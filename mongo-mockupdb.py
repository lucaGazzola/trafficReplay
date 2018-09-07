from mockupdb import *
import pyshark
import sys
import json
import pprint
from scapy.all import *
from scapy.utils import rdpcap

server = MockupDB(port='37379')
port = server.run()
print(port)
#Indirizzo a cui devo spedire i pacchetti mongo con mongoreplay
print(server.uri)
server.autoresponds('isMaster')
server.autoresponds('ping')
#req = server.receives('getnonce').ok(nonce='asdf')

while True:
    request = server.receives()
    print("request---------------------->"+str(request))
    if request.command_name=="getnonce" :
        print("respond")
        cap = pyshark.FileCapture('mongo_capture_test0.pcap', use_json=True)
        out_string = ''
        i = 1
        for pkt in cap:
            layer = 'mongo'
            field_names = set()
            # prendo tutti i layer (protocolli) presenti nel pacchetto
            for current_layer in pkt.layers:
                if not layer or layer == current_layer.__dict__['_layer_name']:
                   # print("\n\ndizionario"+str(current_layer.__dict__) + '\n\n')
                    #out_string += "dizionario:" + str(current_layer.__dict__) + '\n'
                    try:
                        ris = current_layer.__dict__['_all_fields']['mongo.document']['mongo.elements']['mongo.element.name'][0]
                        risp = current_layer.__dict__['_all_fields']['mongo.document']['mongo.elements']['mongo.element.name_tree'][0]['mongo.element.value.string']
                        if ris == 'nonce':
                            print("ris:"+str(ris))
                            print("risp:"+str(risp))
                            server.autoresponds('getnonce',{'nonce':1, 'ok': 1, 'value': risp})
                    except Exception as e:
                        print('Error:'+str(e))
                        continue
       # request.reply({"value": "dbe1f1939ddbb62a"})