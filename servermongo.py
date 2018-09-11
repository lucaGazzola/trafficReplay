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

    #Ogni volta che ricevo una richiesta devo andare a prendere la risposta dal file di report corrispondente
    #Come argomento viene passata la cartella dei file di report per il test

    #Devi trovare un modo per ricevere id della richiesta e metterlo al nome del file
    #In questo modo vado ad aprire il file corrispondente e leggo la parte di reply

    print("Mockup connesso. File passato: "+sys.argv[1])

    #while True:
    print("---------------open server-------------------")
    #if server.got(OpMsg('find', 'test_collection', filter={})):
    if server.got(OpMsg('find', 'test_collection')):
        print("Server:find")
        #Questa risposta è da cambiare con quella giusta letta dal file di report
        server.reply(cursor={'id': 0, 'firstBatch': [{'a': 2}]})
    else:
        cmd = server.receives()
        print(cmd)
        cmd.ok()
    #if server.got('shutdown'):
    server.stop()
    print("---------------close server---------------------")

if __name__ == "__main__":
    main()