import pyshark
import sys
import json
import pprint

appl_ip = "172.19.0.3"
db_ip = "172.19.0.7"


cap = pyshark.FileCapture('capture_without_registry.pcap',use_json=True)
for pkt in cap:
    try:
        if pkt.ip.src == appl_ip and pkt.ip.dst == db_ip:
            print("pacchetto da applicazione a database")
            print(pkt.ip.src)
            print(pkt.ip.dst)
            print(dir(pkt.tcp))
            print(pkt.tcp)
            print(dir(pkt.tcp.stream))
            print(pkt.tcp.stream)
    except:
        continue