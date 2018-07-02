import pyshark
import os
import json
import string
import sys
import re
import collections
import bson
from bson.codec_options import CodecOptions
from pyshark_parser import packet_util
from pyshark_parser import layer_util


def main():
    cap = pyshark.FileCapture(sys.argv[1])
    #cont = 0
    for packet in cap:
        #print("-----------------prova---------------------")
        #Prende tutti i campi del pacchetto mongo
        if not packet:
            print(None)
        layer = 'mongo'
        field_names = set()
        #prendo tutti i layer (protocolli) presenti nel pacchetto
        for current_layer in packet.layers:
            #print("current: "+str(current_layer))
            #print("current: "+current_layer.__dict__['_layer_name'])
            #controllo se layer considerato è MONGO
            if not layer or layer == current_layer.__dict__['_layer_name']:
                #print("layer: "+str(layer))
                #print("elemento current:" + str(current_layer))
                #Tutti i campi di questo livello
                fields = current_layer.__dict__['_all_fields']
                #print(fields)
                for field in fields:
                    field_names.add(field)
                    #print("elemento field:" + fields[field])
                    # if fields["mongo.message_length"] == "194":
                    #     print("elemento field:" + str(field))
                    #Prendo in considerazione il campo "Query"
                    if "Query" in fields[field]:
                    #     #print("field_:"+str(type(fields[field])))
                          fieldquery = fields[field].__dict__['fields']
                    #     #print(type(fieldquery))
                          for p in fieldquery:
                    #         print("elemento lista:"+str(dir(p)))
                            print("elemento attributi:" + str(dir(p)))
                            print("metodo getattribute:" + str(p.__getattribute__('get_default_value')))
                            #print("metodo showname:" + str(p.get_field_by_showname('Elements')))
                            #Nome con cui compare nel pacchetto
                            print("metodo showname:" + str(p.showname))
                            print("get_default_value:"+str(p.get_default_value))

                    #         for k in iter(p.__getattribute__):
                    #             print(str(k))


                        #print(fields[field].__dict__['fields'])
                        #print(dir(fields[field]))
        # layer = 'json'
        # field_names = set()
        # for current_layer in packet.layers:
        #     # print("current: "+str(current_layer))
        #     # print("current: "+current_layer.__dict__['_layer_name'])
        #     if not layer or layer == current_layer.__dict__['_layer_name']:
        #         print("layer: " + str(layer))
        #         for field in current_layer.__dict__['_all_fields']:
        #             field_names.add(field)
        #             print("field_json:" + current_layer.__dict__['_all_fields'][field])
        #print(field_names)
        #print("---------------fine prova ----------------------")



        # if 'MONGO' in str(packet.layers):
        #     if packet.mongo.element_name=="cursor": #insert, update per le request
        #         #dir restituisce l'elenco degli attributi dell'oggetto che viene passato come argomento.
        #         print("---------------------mongo packet------------------------------------")
        #         packetcontent=packet.mongo
        #         print(packetcontent)
        #         print("---------------------attributi mongo packet------------------------------------")
        #         print(dir(packetcontent))
        #         print("---------------------mongo packet data------------------------------------")
        #         print(packetcontent.document)
        #         print(type(packetcontent.document))
        #
        # cont = cont+1

if __name__ == "__main__":
    main()
