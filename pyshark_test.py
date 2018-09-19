import pyshark
import os
import json
import string
import sys
import re
from bson.json_util import loads

def main():

    """
    creates a script that replays an interaction with a docker container in a microservice application
    """
    #Come primo argomento viene passato il nome del file sorgente
        #secondo argomento il file di destinazione
    print("processing file " + sys.argv[1])
    cap = pyshark.FileCapture(sys.argv[1])

    authorized = False
    headers = {'Content-type': 'application/json', "Accept": "application/json"}

    pythonScript = None

    #Pacchetti estratti dal file pcap dove sono memorizzati i pacchetti catturati da un'interfaccia docker
    for packet in cap:
        #REST -> quindi vado a considerare protocollo ad alto livello
        #Controllo che sia interazione diretta con applicazione (porta 8081)
        #Porta 8080 è con gateway quindi non la considero
        if 'HTTP' in str(packet.layers) and 'TCP' in str(packet.layers) and \
                ( packet.tcp.dstport == "8081" or packet.tcp.srcport == "8081" ):
            # print("-------------------------------------per http")
            # print(dir(packet.http))
            # print("-------------------------------------per tcp:")
            # print(dir(packet.tcp))
            # print("-------------------------------------processing file: " + sys.argv[1])
            # print("-------------------------------------dst port: "+str(packet.tcp.dstport))
            # print("-------------------------------------src port: "+str(packet.tcp.srcport))
            # Apro in scrittura il file di destinazione
            #print("-----------------------------------------------")
            #print(str(packet.http.chat))

            if pythonScript is None or pythonScript.closed:
                pythonScript = open(sys.argv[2], 'w')
                write_import(pythonScript)

            if not authorized:
                #headers['Authorization'] = packet.http.authorization
                pythonScript.write("headers=" + str(headers) + "\n\n")
                req_auth(pythonScript)
                authorized = True

            if str(packet.http.chat).startswith('POST'):
                write_post_request(packet, pythonScript)

            if str(packet.http.chat).startswith('GET'):
                write_get_request(packet, pythonScript)

            if str(packet.http.chat).startswith('PUT'):
                 write_put_request(packet, pythonScript)

            #Da Implementare ------------------------------------------
            if str(packet.http.chat).startswith('DELETE'):
                 write_delete_request(packet, pythonScript)

            if str(packet.http.chat).startswith('HTTP'):
                write_assertion(packet, pythonScript)

    if not pythonScript is None:
        pythonScript.close()


def write_import(pythonScript):
    pythonScript.write("import requests\n")
    pythonScript.write("import json\n")
    pythonScript.write("import time\n")
    pythonScript.write("import re\n")
    pythonScript.write("from bson.json_util import loads \n\n")
    pythonScript.write("id_dict = {}\n")


#Mando richiesta autenticazione da gateway per ricevere token
def req_auth(pythonScript):
    pythonScript.write("print('sending post request to http://localhost:8080/api/authenticate')\n")
    pythonScript.write("json_content = {\"username\": \"admin\", \"password\": \"admin\"}\n")
    pythonScript.write("response = requests.post('http://localhost:8080/api/authenticate', data=json.dumps(json_content), headers=headers)\n")
    pythonScript.write("content = re.sub(r'\"id\".*?(?=,)', '\"id\":None', response.content.decode('utf-8'))\n")
    pythonScript.write("data = loads(content)\n")
    pythonScript.write("headers = {'Content-type': 'application/json', 'Accept': 'application/json','Authorization': 'Bearer ' + data['id_token']}\n\n")

def write_get_request(packet, pythonScript):

    """
    writes a get request to a python script
    :param packet: packet request to replay
    :param pythonScript: script to write the request to
    """

    url = 'http://localhost:'

    api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
    api_location = re.sub(r'\?.*', '/', api_location)
    if not api_location.endswith('/'):
        api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location
    #il campo request_uri_query_parameter è presente solo per le get senza passaggio di id
    if not  'request_uri_query_parameter' in packet.http.field_names:
        old_id = url.split("/")
        #Creazione url corretto mettendo url corretto per questo test
        pythonScript.write("url = '" + url + "'\n")
        pythonScript.write("url = url.replace(\""+old_id[len(old_id) - 2]+"\", id_dict['" +old_id[len(old_id) - 2] + "'])\n")
    # hardcoded check, remove
    if url.__contains__('dialog'):
        return

    if not 'request_uri_query_parameter' in packet.http.field_names:
        pythonScript.write("print('sending get request to '+ url)\n")
        pythonScript.write("response = requests.get(url, headers=headers)\n")
    else:
        pythonScript.write("print('sending get request to " + url + "')\n")
        pythonScript.write("response = requests.get('"+url+"', headers=headers)\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n\n")



def write_post_request(packet, pythonScript):

    """
    writes a post request to a python script
    :param packet: packet request to replay
    :param pythonScript: script to write the request to
    """

    url = 'http://localhost:'

    api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
    api_location = re.sub(r'\?.*', '/', api_location)
    if not api_location.endswith('/'):
        api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location
    json_post = packet.http.file_data

    json_post = json_post.replace('null', 'None')
    pythonScript.write("print('sending post request to "+url+"')\n")
    pythonScript.write("json_content = "+json_post+"\n")
    pythonScript.write('print(str(json_content))\n')
    pythonScript.write("response = requests.post('"+url+"', data=json.dumps(json_content), headers=headers)\n")
    pythonScript.write("if response.status_code == 201:\n")
    pythonScript.write("\tprint('created')\n\n")


def write_put_request(packet, pythonScript):

    """
    writes a put request to a python script
    :param packet: packet request to replay
    :param pythonScript: script to write the request to
    """

    url = 'http://localhost:'

    #print(packet.http.authbasic)

    #username=packet.http.authbasic.split(':')[0]
    #password=packet.http.authbasic.split(':')[1]
    #--------------------------------------------Sostituisco con split sullo spazio------------------------------------
    api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
    api_location = re.sub(r'\?.*', '/', api_location).split(':')[0]
    if not api_location.endswith('/'):
        api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location


    pythonScript.write("data = json.loads('"+packet.http.file_data+"')\n")
    pythonScript.write("data['id'] = id_dict[data['id']]\n")
    pythonScript.write("print('sending put request to " + url + "')\n")
    pythonScript.write("response = requests.put('"+url+"', data = json.dumps(data), headers=headers)\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n\n")



def write_delete_request(packet, pythonScript):


    url = 'http://localhost:'

    print("-------------------------------DELETE---------------------------")
    print(packet.http.chat)
    api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
    print(api_location)
    api_location = re.sub(r'\?.*', '/', api_location).split(':')[0]
    if not api_location.endswith('/'):
        api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location
    print(url)
    old_id = url.split("/")
    print(old_id)
    pythonScript.write("url = '" + url + "'\n")
    pythonScript.write("url = url.replace(\"" + old_id[len(old_id) - 2] + "\", id_dict['" + old_id[len(old_id) - 2] + "'])\n")
    pythonScript.write("print('sending delete request to '+ url)\n")
    pythonScript.write("response = requests.delete(url, headers=headers)\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n\n")
    pythonScript.write("assert response.status_code == 200\n\n")

    print("---------------------------------FINE DELETE------------------")




def write_assertion(packet, pythonScript):

    """
    writes an assertion in the replay script to make sure the response to a request is as expected
    :param packet: the response packet to get the assertion from
    :param pythonScript: the script to write the assertion to
    """
    # if packet.http.response_phrase == "OK":
    #     print("ooooook")
    #     print(packet.http.response_phrase)
    #     print(packet.http.response)
    #     print(packet.http.file_data)
    #     stringa = packet.http.file_data[1:len(packet.http.file_data)-1]
    #     dati = stringa.split("},")
    #     print(dati)
    #     print(packet.http.file_data[1:len(packet.http.file_data)-1])
    #     data = loads(packet.http.file_data[1:len(packet.http.file_data)-1])
    #     print(data["id"])
    #Alla fine mi basta solo quello creato
    if packet.http.response_phrase == "Created":
        data = loads(packet.http.file_data)


    if 'file_data' in packet.http.field_names:

        # hardcoded check, remove
        if re.sub(r'\"id\".*?(?=,)', '\"id\":None', packet.http.file_data).__contains__('<div'):
            return
        if packet.http.response_phrase == "Created":
            pythonScript.write("cont = loads(response.content.decode('utf-8'))\n")
            pythonScript.write("id_dict['"+ str(data['id']) +"'] = cont['id']\n\n")
        pythonScript.write("assert response.status_code == " + packet.http.chat[9:12] + "\n\n")
        pythonScript.write("content = re.sub(r'\"id\".*?(?=,)', '\"id\":None',response.content.decode('utf-8'))\n")
        pythonScript.write("assert content == '" + re.sub(r'\"id\".*?(?=,)', '\"id\":None', packet.http.file_data) + "'\n\n")


def db_cleanup(url, pythonScript):

    """
    prints code which cleans the database up
    :param url: container url
    :param pythonScript: script to write the cleanup to
    """

    pythonScript.write("print('setup: cleaning the database')\n")
    pythonScript.write("response = requests.get('"+url+"', headers=headers)\n")
    pythonScript.write("items = json.loads(response.text)\n")
    pythonScript.write("item_ids = []\n")
    pythonScript.write("for item in items:\n")
    pythonScript.write("\turl = '"+url+"/' + str(item['id'])\n")
    pythonScript.write("\tprint('deleting item ' + str(item['id']))\n")
    pythonScript.write("\tr = requests.delete(url, data=json.dumps(item_ids), headers=headers)\n")
    pythonScript.write("\tif r.status_code == 200:\n")
    pythonScript.write("\t\tprint('ok')\n")
    pythonScript.write("print('starting replay')\n")


if __name__ == "__main__":
    main()
