from mockupdb import *
import mockupdb
from collections import OrderedDict
import sys
import json
import pprint
from bson.int64 import Int64
import time
import os
import re
import base64

numbers = re.compile(r'(\d+)')

#Ordinamento per lettura file da cartella
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

#Controllo campi principali di una richiesta
    #test_req contiene la richiesta di confronto
    #req contiene la richiesta da confrontare
    #field contiene il campo da controllare
def check_field(test_req,req,field):
    if field in test_req and field in req:
        if not (test_req[field] == req[field]):
            return False
    else:
        if field in test_req or field in req:
            return False
    return True

#Controllo dei dizionari estratti come elementi dei campi delle richieste
    #dict_check contiene dizionario elemento della richiesta di confronto
    #dict_data contiene dizionario elemento della richiesta da confrontare
def check_dict(dict_check,dict_data):
    if not len(dict_check) == len(dict_data):
        print("non contengono lo stesso numero di elementi")
        return False
    for key, value in dict_check.items():
        if not key in dict_data:
            print("non contengono gli stessi elementi")
            return False
        if key != 'id' and key != '_id':
            if value != dict_data[key]:
                print("non corrispondono")
                return False
    return True


#Controllo comando Delete
    #test_req contiene la richiesta di confronto
    #req contiene la richiesta da confrontare
def cmd_delete(test_req,req):
    #Controllo campo Delete
    if not check_field(test_req,req,'delete'):
        print("campi delete dei comandi delete non corrispondono")
        return False
    #Controllo campo Deletes ---- array di dict
    if 'deletes' in test_req and 'deletes' in req:
        lung = len(test_req['deletes'])
        if lung != len(req['deletes']):
            print("campi deletes con diverso numero di elementi")
            return False
        for i in range(0,lung-1):
            deletes_check = test_req['deletes'][i]
            deletes = req['deletes'][i]
            if not check_dict(deletes_check, deletes):
                print("elementi campi deletes non corrispondendi")
                return False
    else:
        if 'deletes' in test_req or 'deletes' in req:
            print("campi deletes non presenti in entrambe le request")
            return False
    # Controllo campo ordered ---- bool ---to lower case
    if 'ordered' in test_req and 'ordered' in req:
        if not (str(test_req['ordered']).lower() == str(req['ordered']).lower()):
            print("campi ordered di comandi delete non corrispondono")
            return False
    else:
        if 'ordered' in test_req or 'ordered' in req:
            print("campi ordered di comandi delete non presenti in entrambe le richieste")
            return False
    return True

#Controllo comando Update
    #test_req contiene la richiesta di confronto
    #req contiene la richiesta da confrontare
def cmd_update(test_req,req):
    #Controllo campo Update
    if not check_field(test_req,req,'update'):
        print("campi update dei comandi update non corrispondono")
        return False
    #Controllo campo Updates ---- array di dict
    if 'updates' in test_req and 'updates' in req:
        lung = len(test_req['updates'])
        if lung != len(req['updates']):
            print("campi updates con diverso numero di elementi")
            return False
        for i in range(0,lung-1):
            updates_check = test_req['updates'][i]
            updates = req['updates'][i]
            if not check_dict(updates_check, updates):
                print("elementi campi updates non corrispondendi")
                return False
    else:
        if 'updates' in test_req or 'updates' in req:
            print("campi updates non presenti in entrambe le request")
            return False
    # Controllo campo ordered ---- bool ---to lower case
    if 'ordered' in test_req and 'ordered' in req:
        if not (str(test_req['ordered']).lower() == str(req['ordered']).lower()):
            print("campi ordered di comandi update non corrispondono")
            return False
    else:
        if 'ordered' in test_req or 'ordered' in req:
            print("campi ordered di comandi update non presenti in entrambe le richieste")
            return False
    # Controllo campo upsert ---- bool ---to lower case
    if 'upsert' in test_req and 'upsert' in req:
       if not (str(test_req['upsert']).lower() == str(req['upsert']).lower()):
           print("campi upsert di comandi update non corrispondono")
           return False
    else:
        if 'upsert' in test_req or 'upsert' in req:
            print("campi ordered di comandi update non presenti in entrambe le richieste")
            return False
    return True


#Controllo comando Insert
    #test_req contiene la richiesta di confronto
    #req contiene la richiesta da confrontare
def cmd_insert(test_req,req):
    #Controllo campo Insert
    if not check_field(test_req,req,'insert'):
        print("campi insert dei comandi insert non corrispondono")
        return False
    #Controllo campo documents ---- array di dict
    if ('documents' in test_req and 'documents' not in req) or ('documents' not in test_req and 'documents' in req):
        print("campi documents non presenti in entrambe le request")
        return False
    lung = len(test_req['documents'])
    if lung != len(req['documents']):
        print("campi documents con diverso numero di elementi")
        return False
    for i in range(0,lung-1):
        document_check = test_req['documents'][i]
        document = req['documents'][i]
        if not check_dict(document_check, document):
            print("elementi campi documents non corrispondendi")
            return False
    # Controllo campo ordered ---- bool ---to lower case
    if 'ordered' in test_req and 'ordered' in req:
        if not (str(test_req['ordered']).lower() == str(req['ordered']).lower()):
            print("campi ordered di comandi insert non corrispondono")
            return False
    else:
        if 'ordered' in test_req or 'ordered' in req:
            print("campi ordered di comandi insert non presenti in entrambe le richieste")
            return False
    return True


#Controllo comando Count
    #test_req contiene la richiesta di confronto
    #req contiene la richiesta da confrontare
def cmd_count(test_req,req):
    #Controllo campo Count
    if not check_field(test_req,req,'count'):
        print("campi count dei count non corrispondono")
        return False
    #Controllo campo query --- dict
    if ('query' in test_req and 'query' not in req) or ('query' not in test_req and 'query' in req) :
        print("campi query dei count non corrispondono")
        return False
    dict_check = test_req['query']
    dict_data = req['query']
    if not check_dict(dict_check,dict_data):
        print("elementi campi query dei count non corrispondendi")
        return False
    return True

#Controllo comando Find
    #test_req contiene la richiesta di confronto
    #req contiene la richiesta da confrontare
def cmd_find(test_req,req):
    #Controllo campo Limit
    if not check_field(test_req,req,'limit'):
        print("campi limit dei find non corrispondono")
        return False
    #Controllo campo Find
    if not check_field(test_req, req, 'find'):
        print("campi find dei find non corrispondono")
        return False
    #Controllo campo Path
    if not check_field(test_req, req, 'path'):
        print("campi path dei find non corrispondono")
        return False
    #Controllo campo Filter--->dict contenente anche id che non va confrontato--- prendo solo campi significativi
    if ('filter' in test_req and 'filter' not in req) or ('filter' not in test_req and 'filter' in req) :
        print("campi filter dei find non corrispondono")
        return False
    dict_check = test_req['filter']
    dict_data = req['filter']
    if not check_dict(dict_check,dict_data):
        print("elementi campi filter dei find non corrispondendi")
    #Se coincide tutto allora ritorno True
    return True

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def main():
    #Attivazione del Server Mongo
    print("Attivazione Server....")
    server = MockupDB(port='27017')
    server.run()
    print("Server Mongo in esecuzione all'indirizzo "+str(server.address))

    print("----------------Inizializzazione------------------------------")

    getlast=0
    ismaster=0
    buildinfo=0
    saslStart=0
    saslContinue = 0
    folder = "/MockupFolder/Config"
    for conf in os.listdir(folder):
        if getlast == 0 and "getlasterror" in str(conf):
            getlast = getlast + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                getlasterror_reply = OpReply(data["reply_data"])
                print("a getlasterror rispondo con" + str(getlasterror_reply))
                server.autoresponds('getlasterror', getlasterror_reply)

        if ismaster == 0 and "isster" in str(conf):
            print("preso file: "+str(conf))
            ismaster = ismaster + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                ismaster_reply = OpReply(data["reply_data"])
                print("a ismaster rispondo con" + str(ismaster_reply))
                server.autoresponds('ismaster', ismaster_reply)

        if buildinfo == 0 and (("buildInfo" in str(conf)) or ("buildinfo" in str(conf))):
            buildinfo = buildinfo + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                buildinfo_reply = OpReply(data["reply_data"])
                print("a buildinfo rispondo con"+str(buildinfo_reply))
                server.autoresponds('buildInfo', buildinfo_reply)
                server.autoresponds('buildinfo', buildinfo_reply)

        if saslStart == 0 and "saslStart" in str(conf):
            saslStart = saslStart + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                bin_data = "cj07JVxUUDM8TXVvd08hZXE9cWondHBSZElpSmZOb21mOHluUitjMmR0Y0x3RGtYSE5pWjVXWU9SZSxzPVBzdEJqdWpXQjZEdkR6Kzk2LysxR0E9PSxpPTEwMDAw".encode("ascii")
                #data["reply_data"]["payload"] = int(text_to_bits(bin_data))
                data["reply_data"]["payload"] = base64.decodebytes(bin_data)
                print(data["reply_data"])
                saslStart_reply = OpReply(data["reply_data"])
                server.autoresponds('saslStart', saslStart_reply)

        if saslContinue == 0 and "saslContinue" in str(conf):
            saslContinue = saslContinue + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                if str(data["reply_data"]["done"]) == "false":
                    print("è su false")
                    bin_data = ''.encode("ascii")
                else:
                    print("è su true")
                    bin_data = "dj0zb1A2enh5anBXSW5xc25nWllzN2lYZWJ3S289".encode("ascii")
                #data["reply_data"]["payload"] = int(text_to_bits(bin_data))
                data["reply_data"]["payload"] = base64.decodebytes(bin_data)
                saslContinue_reply = OpReply(data["reply_data"])
                server.autoresponds('saslContinue', saslContinue_reply)


        if getlast == 1 and ismaster == 1 and buildinfo == 1 and saslContinue == 1 and saslStart == 1:
            break


    if(ismaster == 0):
        print("ismaster automatico")
        opmsgreply = mockupdb.make_op_msg_reply(OrderedDict([('maxWireVersion', 6), ('minWireVersion', 0), ('ok', 1.0)]))
        server.autoresponds('ismaster',opmsgreply)
    if (buildinfo == 0):
        print("buildinfo automatico")
        server.autoresponds('buildInfo')
        server.autoresponds('buildinfo')
    if (getlast == 0):
        print("getlasterror automatico")
        server.autoresponds('getlasterror')
    if (saslStart == 0):
        print("saslstart automatico")
        server.autoresponds('saslStart')
    if (saslContinue == 0):
        print("saslcontinue automatico")
        server.autoresponds('saslContinue')
    server.autoresponds('ping')

    find_list = []
    insert_list = []
    delete_list = []
    folder = "/MockupFolder/CMDs"
    for command in os.listdir(folder):
        if "find" in str(command):
            with open(str(folder)+'/'+str(command)) as file_data:
                data = json.load(file_data)
                data["reply_data"]["cursor"]["id"] = Int64(0)
                find_list.append(OpReply(data["reply_data"]))
        if "insert" in str(command):
            with open(str(folder)+'/'+str(command)) as file_data:
                data = json.load(file_data)
                insert_list.append(OpReply(data["reply_data"]))
        if "delete" in str(command):
            with open(str(folder)+'/'+str(command)) as file_data:
                data = json.load(file_data)
                delete_list.append(OpReply(data["reply_data"]))

    count_find = 0
    count_insert = 0
    count_delete = 0
    #Altrimenti attendo di ricevere find, insert e delete per inizializzazione
    #Magari non sempre sono precisamente tre quindi termino quando ne ho ricevuto almento uno di ogni tipo
    while not (count_delete == len(delete_list) and count_find == len(find_list) and count_insert == len(insert_list)):
        cmd = server.receives(timeout=3000)
        if str(cmd.command_name) == "find":
            cmd.replies(find_list[count_find])
            count_find = count_find + 1
        else:
            if str(cmd.command_name) == "insert":
                cmd.replies(insert_list[count_insert])
                count_insert = count_insert + 1
            else:
                if str(cmd.command_name) == "delete":
                    cmd.replies(delete_list[count_delete])
                    count_delete = count_delete + 1
                else:
                    general_reply = OpReply({
                        "n": 1,
                        "ok": 1.0
                    })
                    cmd.replies(general_reply)

    print("----------------Inizializzazione Terminata------------------------------")

    print("in attesa di comando")
    cmd = server.receives(timeout=100000)
    print("ricevuto: " + str(cmd))
    num_rep = 1
    while True:
        print("-----------------TEST "+str(num_rep)+"----------------------")
        # Adesso ricevo richieste dall'applicazione, controllo che siano corrette e invio risposte
        file = open('ActualFileTest.txt', 'r')
        folder_name = file.read()
        print(folder_name)
        folder_name = folder_name.strip('\n')
        print(folder_name)
        file.close()
        folder = str(folder_name)+"CMDs"
        num_rep = num_rep + 1
        for command in sorted(os.listdir(folder), key=numericalSort):
            #Controllo che il contenuto della richiesta sia corretto
            with open(str(folder)+'/'+str(command)) as file_data:
                data = json.load(file_data)
                if cmd.command_name == "find" and 'cursor' in  data["reply_data"] and 'id' in data["reply_data"]["cursor"] \
                        and '$numberLong' in data["reply_data"]["cursor"]["id"] :
                    number_long = data["reply_data"]["cursor"]["id"]["$numberLong"]
                    data["reply_data"]["cursor"]["id"] = Int64(number_long)

                #------------da qua confronto richiesta-------------
                request_check = data["request_data"]
                request = json.loads(str(cmd))
                print("Controllo correttezza richiesta...")
                dispatcher = {'update': cmd_update, 'insert':cmd_insert, 'delete':cmd_delete, 'find':cmd_find, 'count': cmd_count}
                ris = dispatcher[cmd.command_name](request_check,request)
                print(ris)
                assert ris == True
                print("Success!")

            #Se corretto mando la risposta contentuta nel file di report
                response = OpReply(data["reply_data"])
                print("risposta con: " + str(response))
                cmd.replies(response)
            print("in attesa di comando")
            cmd = server.receives(timeout=100000)
            print("ricevuto: " + str(cmd))




if __name__ == "__main__":
    main()