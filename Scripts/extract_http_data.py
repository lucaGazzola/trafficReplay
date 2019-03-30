import pyshark
import os
import json
import string
import sys
import re
from bson.json_util import loads


def main():
    # Come primo argomento viene passato il nome del file sorgente
    # secondo argomento il file di destinazione
    print("processing file " + sys.argv[1])
    cap = pyshark.FileCapture(sys.argv[1])

    appmock = sys.argv[2]

    appip = sys.argv[3]

    response_json = {}
    #Controllo se il file contenente il json con le risposte del mockup esiste
    try:
        with open(sys.argv[4]) as file_data:
            response_json = json.load(file_data)
    except FileNotFoundError:
        response_json['port'] = 5000
        response_json['protocol'] = "http"
        response_json['stubs'] = []

        #La risposta a /uaa/oauth/token deve essere sempre la stessa
        json_data = {}
        json_data_cont = {}
        json_header = {}
        json_data_cont['statusCode'] = 200
        json_header["Content-Type"] = "application/json"
        json_data_cont['headers'] = {"Content-Type": "application/json;charset=UTF-8", "Cache-Control": "no-store",
                                          "Pragma": "no-cache", "X-Content-Type-Options": "nosniff",
                                          "X-XSS-Protection": "1; mode=block", "X-Frame-Options": "DENY",
                                          "Transfer-Encoding": "chunked"}
        json_data_cont['body'] = {"access_token": "1b4270ff-d035-4d17-a2ff-9b350dea66be", "token_type": "bearer",
                                       "expires_in": 43199, "scope": "server"}
        json_data['is'] = json_data_cont
        json_stub = {}
        response_json['stubs'].append(json_stub)
        response_json['stubs'][0]['responses'] = []
        response_json['stubs'][0]['predicates'] = []
        response_json['stubs'][0]['responses'].append(json_data)
        json_data_req = {}
        json_data_eq = {}
        json_data_req['method'] = "POST"
        json_data_req['path'] = "/uaa/oauth/token"
        json_data_eq['equals'] = json_data_req
        response_json['stubs'][0]['predicates'].append(json_data_eq)

    shellfile = open(sys.argv[4], "w")

    #Dizionario contenente tutte le richieste ---> come chiave andrò ad utilizzare il tcp.stream
    dict_request={}

    # Pacchetti estratti dal file pcap dove sono memorizzati i pacchetti catturati da un'interfaccia docker
    for packet in cap:

        # Controllo prendendo la lista degli ip
            # print(packet.ip.dst)
            # print(packet.ip.src)
            # print(appip)
            # print(port)
            # print(packet.tcp.dstport)
            # print(packet.tcp.srcport)

        #print(dir(packet.tcp))
        if 'HTTP' in str(packet.layers) and 'TCP' in str(packet.layers) and \
                ( packet.ip.src == appmock or packet.ip.dst == appmock ) and \
                ( packet.ip.src == appip or packet.ip.dst == appip ):
            if str(packet.http.chat).startswith('POST'):
                dict_request[packet.tcp.stream] = packet
                #stampa(packet)
            if str(packet.http.chat).startswith('GET'):
                dict_request[packet.tcp.stream] = packet
                #stampa(packet)
            if str(packet.http.chat).startswith('HTTP'):
                print("ENTRO")
                if packet.tcp.stream in dict_request:
                    write_data(packet,response_json,dict_request)
    shellfile.write(json.dumps(response_json))
    shellfile.close()


def stampa(packet):
    print("viaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(packet.http.field_names)
    if "request_version" in packet.http.field_names:
        print(packet.http.request_version)
        print("-------request_version------")
    if "request_full_uri" in packet.http.field_names:
        print(packet.http.request_full_uri)
        print("-------request_full_uri------")
    if "request_line" in packet.http.field_names:
        print(packet.http.request_line)
        print(packet.http.request_line.split(":")[1])
        print("-------request_line------")
    if "request_uri" in packet.http.field_names:
        print(packet.http.request_uri)
        print("-------request_uri------")
    if "request_in" in packet.http.field_names:
        print(packet.http.request_in)
        print("-------request_in------")
    if "request" in packet.http.field_names:
        print(packet.http.request)
        print("-------Request------")
    if "request_method" in packet.http.field_names:
        print(packet.http.request_method)
        print("-------request_method------")
    if "chat" in packet.http.field_names:
        print(packet.http.chat)
        print("-------chat------")
    if "file_data" in packet.http.field_names:
        print(packet.http.file_data)
    else:
        print("no data")


def write_data(packet, response_json, dict_request):
    """
    writes an assertion in the replay script to make sure the response to a request is as expected
    :param packet: the response packet to get the assertion from
    :param shellfile: the script to write the assertion to
    """

    json_data = {}
    json_data_cont = {}
    json_header = {}
    json_data_cont['statusCode'] = str(packet.http.response_code)
    json_header["Content-Type"] = "application/json"
    json_data_cont['headers'] = json_header
    if "file_data" in packet.http.field_names:
        json_data_cont['body'] = loads(packet.http.file_data)
    json_data['is'] = json_data_cont
    #json_behavior = {}
    #json_behavior['repeat'] = 1
    #json_data['_behaviors'] = json_behavior
    i = len(response_json['stubs'])
    json_stub = {}
    response_json['stubs'].append(json_stub)
    response_json['stubs'][i]['responses'] = []
    response_json['stubs'][i]['predicates'] = []
    response_json['stubs'][i]['responses'].append(json_data)

    json_data_req={}
    json_data_req2 = {}
    json_data_eq={}
    json_data_cont = {}
    json_data_req['method'] = dict_request[packet.tcp.stream].http.request_method
    json_data_req['path'] = dict_request[packet.tcp.stream].http.request_uri
    header_req = {}
    header_req['Authorization'] = dict_request[packet.tcp.stream].http.request_line.split(": ")[1].replace('\\xd\\xa', '')
    #json_data_req2['headers'] = header_req
    json_data_req['headers'] = header_req
    if "file_data" in dict_request[packet.tcp.stream].http.field_names:
        print("file_data:---------------------")
        print(dict_request[packet.tcp.stream].http.file_data)
        try:
            json_data_req['body'] = loads(dict_request[packet.tcp.stream].http.file_data)
        except ValueError:
            json_data_req['body'] = str(dict_request[packet.tcp.stream].http.file_data)
    json_data_eq['equals'] = json_data_req
    json_data_cont['contains'] = json_data_req2
    response_json['stubs'][i]['predicates'].append(json_data_eq)
    response_json['stubs'][i]['predicates'].append(json_data_cont)



if __name__ == "__main__":
    main()
