from mockupdb import *
import pyshark
import sys
import json
import pprint

def main():
    server = MockupDB(port='37379')
    port = server.run()
    file = open("server_uri.txt","w")
    file.write(server.uri)
    file.close()
    print(port)
    # Indirizzo a cui devo spedire i pacchetti mongo con mongoreplay
    print(server.uri)
    responder = server.autoresponds('ismaster', maxWireVersion=6)
    server.autoresponds('ping')
    responder = server.autoresponds(OpMsg('find', 'collection'),{'cursor': {'id': 0, 'firstBatch': [{'a': 1}, {'a': 2}]}})
    while True:
        if server.got(OpMsg('find', 'test_collection', filter={})):
            print("Entro per la find................")
            #Questa risposta è da cambiare con quella giusta letta dal file di report
            server.reply(cursor={'id': 0, 'firstBatch': [{'a': 2}]})
        else:
            cmd = server.receives()
            print(cmd)
            cmd.ok()

if __name__ == "__main__":
    main()