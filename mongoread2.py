import os
import pcapy as p
from scapy.all import *
from getHTTPHeaders import HTTPHeaders, extractText

data = sys.argv[1]
a = rdpcap(data)
sessions = a.sessions()
print("Inizio")
for session in sessions:
    http_payload = ""
    for packet in sessions[session]:
        print(packet.show())
        #print(packet.summary())
        try:
            #print(packet[TCP].dport)
            if packet[TCP].dport == 8081 or packet[TCP].sport == 8080:
                http_payload += str(packet[TCP].payload)
        except:
            pass
        headers = HTTPHeaders(http_payload)
    if headers is None:
        print("headers is none")
        continue
    text = extractText(headers,http_payload)
    if text is not None:
         print (text)
    else:
        print("is none")