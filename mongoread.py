import pyshark
import os
import json
import string
import sys
import re


def main():
    cap = pyshark.FileCapture(sys.argv[1])
    cont = 0
    indexvalue = 0
    indextype = 0
    for packet in cap:
        if 'MONGO' in str(packet.layers):
            if packet.mongo.element_name=="cursor": #insert, update per le request
                #dir restituisce l'elenco degli attributi dell'oggetto che viene passato come argomento.
                print("---------------------mongo packet------------------------------------")
                packetcontent=str(packet.mongo);
                print(packetcontent)
                line = packetcontent.split('\n')
                lung = len(line) - 1
                for i in range(0,lung):
                    #Leggo linea per linea
                    print("linea:"+line[i]+"\n")
                    #Elimino tutti gli spazi
                    value=line[i].strip()
                    value=value.replace(" ","")
                    content=value.split(":")
                    print(content)
                    #if(len(content
                    #  )==2)

                    # print("---------------------attributi mongo packet getitem------------------------------------")
                    # print(type(packetcontent))
                    # print(type(packetcontent.element_name))
                    # print(packetcontent.element_name.size)
                    # print(packetcontent.document_length)
                    # print(packetcontent.__getattribute__("Document"))
                    print("---------------------mongo packet fields------------------------------------")
                    fieldnames = packet.mongo.field_names
                    print(fieldnames)
                    print("---------------------mongo packet document-----------------------------------")
                    print(packet.mongo.document)
                    print("---------------------mongo packet opcode------------------------------------")
                    print(packet.mongo.opcode)
                    print("---------------------mongo packet raw_mode------------------------------------")
                    print(packet.mongo.raw_mode)
                    print("---------------------attributi di elements------------------------------------")
                    print(dir(packet.mongo.elements))
                    print("---------------------tutti i campo di elements------------------------------------")
                    print(packet.mongo.elements.all_fields)
                    # print("---------------------TCP------------------------------------")
                    # print(dir(cap[cont].tcp))
                    # print("--------------------TCP PAYLOAD-------------------------------------")
                    # print(dir(cap[cont].tcp.payload))
                    # print("---------------------MONGO------------------------------------")
                    # print(dir(cap[cont].mongo))
                    # print("--------------------MONGO Response-------------------------------------")
                    # print(dir(cap[cont].mongo.response_to))
                    # print("--------------------Content-------------------------------------")
                    # print(cap[cont].mongo.response_to.decode("ascii", "ignore"))
                    # print("--------------------MONGO Query-------------------------------------")
                    # print(get(cap[cont].mongo,"query",None))
                    # print("--------------------Content-------------------------------------")
                    # print(cap[cont].mongo.query)
                    # print("--------------------MONGO __getitem__--------------------------------")
                    # print(dir(cap[cont].mongo.query.__getitem__(1)))

                    # if value.startswith("Value:"):
                    #      print("valore letto "+value)
                print("---------------------attributi mongo packet------------------------------------")
                print(dir(packet.mongo))
        cont = cont+1

if __name__ == "__main__":
    main()
