import pyshark
import os
import json
import string
import sys
import re

correct = False

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
    global correct

    #apro in scrittura il file di destinazione
    pythonScript = open(sys.argv[2], 'w')
    pythonScript.write("import requests\n")
    pythonScript.write("import json\n")
    pythonScript.write("import time\n")
    pythonScript.write("import re\n\n")

    #Pacchetti estratti dal file pcap dove sono memorizzati i pacchetti catturati da un'interfaccia docker
    for packet in cap:
        if 'HTTP' in str(packet.layers):
            # print(packet.http)
            if not authorized:
                headers['Authorization'] = packet.http.authorization
                pythonScript.write("headers=" + str(headers) + "\n\n")
                authorized = True

            if str(packet.http.chat).startswith('POST'):
                write_post_request(packet, pythonScript)
                correct = True

            if str(packet.http.chat).startswith('GET'):
                write_get_request(packet, pythonScript)
                correct = True

            #if str(packet.http.chat).startswith('PUT'):
                # print(packet.http._all_fields)
                #write_put_request(packet, pythonScript)

            if str(packet.http.chat).startswith('HTTP'):
                write_assertion(packet, pythonScript)
                correct = True

    pythonScript.close()
    if not correct:
        try:
            os.remove(sys.argv[2])
        except OSError:
            pass


def write_get_request(packet, pythonScript):

    """
    writes a get request to a python script
    :param packet: packet request to replay
    :param pythonScript: script to write the request to
    """

    global correct

    url = 'http://localhost:'

    api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
    print("------inizio-------")
    print(api_location)
    api_location = re.sub(r'\?.*', '/', api_location)
    print(api_location)
    print("------fine-------")
    if not api_location.endswith('/'):
        api_location += '/'
    print('get')
    print(api_location)
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location

    # hardcoded check, remove
    if url.__contains__('dialog'):
        correct = False
        return

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
    print("------inizio-------")
    print(api_location)
    api_location = re.sub(r'\?.*', '/', api_location)
    print(api_location)
    print("------fine-------")
    if not api_location.endswith('/'):
        api_location += '/'
    print('post')
    print(api_location)
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

    username=packet.http.authbasic.split(':')[0]
    password=packet.http.authbasic.split(':')[1]

    api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
    api_location = re.sub(r'\?.*', '/', api_location).split(':')[0]
    if not api_location.endswith('/'):
        api_location += '/'
    print('put')
    print(api_location)
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location

    pythonScript.write("print('sending get request to " + url + "')\n")
    pythonScript.write("response = requests.get('"+url+"', headers=headers, auth=HTTPBasicAuth('"+username+"', '"+password+"'))\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n\n")


def write_assertion(packet, pythonScript):

    """
    writes an assertion in the replay script to make sure the response to a request is as expected
    :param packet: the response packet to get the assertion from
    :param pythonScript: the script to write the assertion to
    """


    if 'file_data' in packet.http.field_names:

        # hardcoded check, remove
        if re.sub(r'\"id\".*?(?=,)', '\"id\":None', packet.http.file_data).__contains__('<div'):
            return

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
