import pyshark
import sys
import json
import pprint
#Come primo argomento passo interfaccia dove mi metto in ascolto
#br-3a3ccaf7e2ef
#cap = pyshark.LiveCapture(interface=sys.argv[1],use_json=True)
cap = pyshark.FileCapture('capture.pcap',use_json=True)
#cap.sniff(packet_count=500)
out_string = ''
i = 1
#for pkt in cap.sniff_continuously():
for pkt in cap:
    layer = 'mongo'
    field_names = set()
    # prendo tutti i layer (protocolli) presenti nel pacchetto
    for current_layer in pkt.layers:
        # controllo se layer considerato è MONGO

        if not layer or layer == current_layer.__dict__['_layer_name']:
            # print(pkt.ip.src)
            # print(pkt.ip.dst)
            # print("opcode-->"+pkt.mongo.opcode)
            # Prendo pacchetto che hanno opcode != 1 (codice di risposta)
            print("dizionario:" + str(current_layer.__dict__) + '\n')
            out_string += "dizionario:" + str(current_layer.__dict__) + '\n'
    #if not pkt.mongo.opcode == '1':
            #print(pkt.ip.src)
            #print(pkt.ip.dst)
            out_file = open("Mongo_Request_pkts.txt", "w")
            print("Chiave-Valore:")
            out_string +="Chiave-Valore:\n"

            #Vado a prendere tutti i campi
            #Controllo se trovo all_fields->query
            #se lo trovo allora vado a cercare Elements->Documents->Document->Element->Document->Elements
            for keys, values in current_layer.__dict__.items():
                out_string += "chiave1: "+str(keys) + "\n"
                print("chiave1:" + keys)
                if keys == "_all_fields":
                    for k1, v1 in current_layer.__dict__[keys].items():
                        out_string += "chiave2: " + str(k1) + "\n"
                        print("chiave2:" + k1)
                        if k1 == "mongo.query":
                            for k2, v2 in current_layer.__dict__[keys][k1].items():
                                out_string += "chiave3: " + str(k2) + "\n"
                                print("chiave3:" + k2)
                            if k2 == "mongo.elements":
                                for k3, v3 in current_layer.__dict__[keys][k1][k2].items():
                                    out_string += "chiave4: " + str(k3) + "\n"
                                    out_string += "contenuto4: " + str(v3) + "\n"
                                    print("chiave4:" + k3)
                                    print("contenuto4:" + str(v3))
                                if k3 == "mongo.element.name_tree":
                                    iterator1 = iter(current_layer.__dict__[keys][k1][k2][k3])
                                    var = next(iterator1, None)
                                    classeok = False
                                    while  not (var is None):
                                        dict1 = var
                                        out_string += "tipo chiave5: " + str(type(var)) + "\n"
                                        out_string += "chiave5: " + str(var) + "\n\n"
                                        print("chiave5:" + str(var))
                                        print("tipo chiave5: " + str(type(var)))
                                        var = next(iterator1, None)
                                        if isinstance(dict1, dict):
                                           if dict1["mongo.element.type"] == "0x00000002" and not classeok:
                                             classe = dict1["mongo.element.value.string"]
                                             classeok = True
                                           if dict1["mongo.element.type"] == "0x00000004":
                                             for k4, v4 in dict1.items():
                                                 out_string += "chiave6: " + str(k4) + "\n"
                                                 out_string += "contenuto6: " + str(v4) + "\n\n"
                                                 print("chiave6:" + k4)
                                                 print("contenuto6:" + str(v4))
                                                 if k4 == "mongo.document":
                                                     for k5, v5 in dict1[k4].items():
                                                         out_string += "chiave7: " + str(k5) + "\n"
                                                         out_string += "contenuto7: " + str(v5) + "\n\n"
                                                         print("chiave6:" + k5)
                                                         print("contenuto6:" + str(v5))
                                                         if k5 == "mongo.elements":
                                                             for k6, v6 in dict1[k4][k5].items():
                                                                 out_string += "chiave8: " + str(k6) + "\n"
                                                                 out_string += "contenuto8: " + str(v6) + "\n\n"
                                                                 print("chiave8:" + k6)
                                                                 print("contenuto8:" + str(v6))
                                                                 if k6 == "mongo.element.name_tree":
                                                                     for k7, v7 in dict1[k4][k5][k6].items():
                                                                         out_string += "chiave9: " + str(k7) + "\n"
                                                                         out_string += "contenuto9: " + str(v7) + "\n\n"
                                                                         print("chiave9:" + k7)
                                                                         print("contenuto9:" + str(v7))
                                                                     if k7 == "mongo.document":
                                                                         for k8, v8 in dict1[k4][k5][k6][k7].items():
                                                                             out_string += "chiave10: " + str(k8) + "\n"
                                                                             out_string += "contenuto10: " + str(
                                                                                 v8) + "\n\n"
                                                                             print("chiave10:" + k8)
                                                                             print("contenuto10:" + str(v8))
                                                                             if k8 == "mongo.elements":
                                                                                 for k9, v9 in dict1[k4][k5][k6][
                                                                                     k7][k8].items():
                                                                                     #Ora sono dove gli elementi
                                                                                     out_string += "chiave11: " + str(
                                                                                         k9) + "\n"
                                                                                     out_string += "contenuto11: " + str(
                                                                                         v9) + "\n\n"
                                                                                     print("chiave11:" + k9)
                                                                                     print("contenuto11:" + str(v9))
                                                                                     if k9 == "mongo.element.name":
                                                                                         #etichette contenuto prossimo campo
                                                                                         listaet = v9
                                                                                     if k9 == "mongo.element.name_tree":
                                                                                         lung = len(v9)
                                                                                         out_string += "listaet:" + str(listaet) + "\n"
                                                                                         out_string += "lunghezza:" + str(lung)+"\n"
                                                                                         out_string += "lunghezza2:" + str(
                                                                                             len(listaet)) + "\n"
                                                                                         listael = v9
                                                                                         for cont in range(0,lung):
                                                                                             out_string +="elemento:"+str(listaet[cont])+"\n"
                                                                                             out_string += "contenuto:" + str(listael[cont]) + "\n\n"

            out_file.write(out_string)
            i = i + 1
            #print(pkt)
cap.close()
