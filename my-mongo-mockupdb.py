from scapy.all import *
from scapy.utils import rdpcap
# import pyshark
# import sys
# import json
# import pprint

def intercept(pkt):
     #pkts=rdpcap("mongo_capture.pcap")  # could be used like this rdpcap("filename",500) fetches first 500 pkts
    #for cap in pkts:
        #vado a prelevare informazioni da pkt
        #vado a prelevare info da cap
        #confronto
        #invio risposta
    print(pkt.summary())
    print(dir(pkt[TCP]))

    print(pkt[TCP].seq)
    print(pkt[TCP].ack)
    print("\n\n")

def main():
    sniff(iface='lo', filter='port 37379', prn=intercept)
    # print("avvio")
    # cap = pyshark.LiveCapture(interface='lo', use_json=True, bpf_filter = 'port 37379')
    # print("ricezione")
    #
    # for pkts in cap:
    #     print(pkts.layers)

if __name__ == '__main__':
   main()