import pyshark
import sys
#Come primo argomento passo interfaccia dove mi metto in ascolto
#br-3a3ccaf7e2ef
cap = pyshark.LiveCapture(interface=sys.argv[1])
#cap.sniff(packet_count=500)
out_string = ''
i = 1
for pkt in cap.sniff_continuously():
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
            if not pkt.mongo.opcode == '1':
                print(pkt.ip.src)
                print(pkt.ip.dst)
                out_file = open("Mongo_Request_pkts.txt", "w")
                out_string += "Packet #         " + str(i)
                out_string += "\n"
                out_string += str(pkt)
                out_string += "\n"
                out_file.write(out_string)
                i = i + 1
                print(pkt)
cap.close()
