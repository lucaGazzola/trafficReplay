#Creo Client Mongo


from mockupdb import *
import pyshark
import sys
import json
import pprint
from pymongo import MongoClient
from bson.json_util import loads

def main():
    #Come primo argomento mi viene passato il file contenente i report
    with open(sys.argv[1], 'r') as f:
        array = json.load(f)

    operation = array['op']

    #Come secondo argomento passo la uri del Server (magari lo faccio memorizzare su un file dal server quando lo creo)
    client = MongoClient(sys.argv[2])
    collection = client.db.test_collection

    print("Test: attesa connessione con mockup...")
    client.db.command('ping')
    print("Test:connesso")

    print("nome del database: "+client.db.name)


    #Come primo comando mando il request_id a cui fare riferimento
    #client.db.command("info","1234")


    # if sys.argv[2] == "first":
    #     #se la prima operazione è una find allora faccio inizilizzazione
    #     if operation == "command":
    #         operation = array['command']
    #         operation_test = arraytest['command']
    #         print("\n\noperation= " + operation + " optest= " + operation_test + "\n")
    #         assert operation == operation_test
    #         print("operazione di ricerca")
    #         return
    #     #Altrimenti inizializzo a database vuoto
    #     else:
    #         #non ci deve essere il return
    #Se sono fuori dal primo if significa che devo trattare le altre operazioni normalmente

    #Se è un'operazione di insert vado ad estrarre i dati da inserire dal file di report e richiedo inserimento al server
    if operation == "insert":
        print("---------------------------------open client-----------------------------------------")
        print("operazione di inserimento")
        #Estrazione informazioni dal file di report
        req_data = array['request_data']
        doc = req_data['documents']
        doc_string = str(doc)
        #print("replace...")
        doc_string = doc_string.replace("\'", "\"")
        #print("document:"+doc_string)
        data = loads(doc_string)
        #print("data:"+str(data))
        # for doc in data:
        #     collection.insert(doc)
        future = go(collection.insert_one, data[0])
        #future = go(collection.insert_one, {'_id': 1, "name": 'prod1', "price": '12.33'})
        write_result = future()
        print("risultato inserimento:"+str(write_result))
        print("id inserito "+str(write_result.inserted_id))


    #Se è un'operazione di insert vado ad estrarre i dati da aggiornare e quelli che vengono usati per aggiornare
    if operation == "update":
        print("-------------------------------open client-------------------------------------------")
        print("operazione di aggiornamento")
        req_data = array['request_data']
        updates = req_data['updates']
        for i in range(0, len(updates)):
            #print("updates: "+str(i)+" "+str(updates[i]))
            for key, value in updates[i].items():
                if key == 'u':
                    new_item = str(updates[i][key])
                    new_item = new_item.replace("\'", "\"")
                    #print("new_item:"+ new_item)
                    data_new = loads(new_item)
                if key == 'q':
                    old_item = str(updates[i][key])
                    old_item = old_item.replace("\'", "\"")
                    #print("old_item:" + old_item)
                    data_old = loads(old_item)
                if key == 'upsert':
                    upsert = updates[i][key]
        if updates:
            collection.update( data_old, data_new, upsert=True)
        else:
            collection.update(data_old, data_new, upsert=False)

    #Se è un'operazione di cancellazione estraggo id elemento da eliminare
    if operation == "delete":
        print("----------------------------------open client----------------------------------------")
        print("operazione di delete")
        req_data = array['request_data']
        deletes = req_data['deletes']
        for i in range(0, len(deletes)):
             for key, value in deletes[i].items():
                 if key == 'q':
                     delete_item = str(deletes[i][key])
                     delete_item = delete_item.replace("\'", "\"")
                     print("delete_item:" + delete_item)
                     data_delete = loads(delete_item)
        collection.remove(data_delete)

    #Se è un'operazione di ricerca devo settare filtri e impostare formato risultato
    if operation == "command":
        operation = array['command']
        if operation == "find":
            print("-------------------------------open client-------------------------------------------")
            print("operazione di ricerca")
            req_data = array['request_data']
            filt = req_data['filter']
            print("Filter:"+str(filt))
            # req_item = str(req_data)
            # req_item = req_item.replace("\'", "\"")
            # print("request_data:"+str(req_item))
            #pprint.pprint(collection.find())
            cursor = collection.find(filt)
            print(str(cursor))
            try:
                record = cursor.next()
                print(str(record))
            except StopIteration:
                print("Empty cursor!")
            # for document in cursor:
            #     pprint(document)
    #client.db.command('shutdown')
    client.close()
    print("---------------------------------------------close client----------------------------------")
if __name__ == "__main__":
    main()



