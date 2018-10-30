from mockupdb import *
import sys
import json
import pprint
from bson.int64 import Int64
import time
import os
import re

numbers = re.compile(r'(\d+)')

def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def main():
    #Attivazione del Server Mongo
    print("Attivazione Server....")
    server = MockupDB(port='37379')
    server.run()
    print("Server Mongo in esecuzione all'indirizzo "+str(server.address))

    print("----------------Inizializzazione------------------------------")

    getlast=0
    ismaster=0
    buildinfo=0
    folder = "/MockupFolder/Config"
    for conf in os.listdir(folder):
        if getlast == 0 and "getlasterror" in str(conf):
            getlast = getlast + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                getlasterror_reply = OpReply(data["reply_data"])
                server.autoresponds('getlasterror', getlasterror_reply)

        if ismaster == 0 and "ismaster" in str(conf):
            ismaster = ismaster + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                ismaster_reply = OpReply(data["reply_data"])
                server.autoresponds('ismaster', ismaster_reply)

        if buildinfo == 0 and (("buildInfo" in str(conf)) or ("buildinfo" in str(conf))):
            buildinfo = buildinfo + 1
            with open(str(folder)+'/'+str(conf)) as file_data:
                data = json.load(file_data)
                buildinfo_reply = OpReply(data["reply_data"])
                server.autoresponds('buildInfo', buildinfo_reply)
                server.autoresponds('buildinfo', buildinfo_reply)

        if getlast == 1 and ismaster == 1 and buildinfo == 1:
            break


    if(ismaster == 0):
        server.autoresponds('ismaster')
    if (buildinfo == 0):
        server.autoresponds('buildInfo')
        server.autoresponds('buildinfo')
    if (getlast == 0):
        server.autoresponds('getlasterror')
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
        folder = "/reports"+str(num_rep)+"/CMDs"
        num_rep = num_rep + 1
        for command in sorted(os.listdir(folder), key=numericalSort):
            #Controllo che il contenuto della richiesta sia corretto
            print("file: "+str(command))
            with open(str(folder)+'/'+str(command)) as file_data:
                data = json.load(file_data)
                print("confronto con: "+str(data["request_data"]))
                if cmd.command_name == "find" and 'cursor' in  data["reply_data"] and 'id' in data["reply_data"]["cursor"]:
                    data["reply_data"]["cursor"]["id"] = Int64(0)
            #Se corretto mando la risposta contentuta nel file di report
                response = OpReply(data["reply_data"])
                print("risposta con: " + str(response))
                cmd.replies(response)
            print("in attesa di comando")
            cmd = server.receives(timeout=100000)
            print("ricevuto: " + str(cmd))




if __name__ == "__main__":
    main()
