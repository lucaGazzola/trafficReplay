import pyshark
import os
import json
import string
import sys
import re

def main():

    """
    creates a script that replays an interaction with a docker container in a microservice application
    """
    #Come primo argimento viene passato il nome del file sorgente
        #secondo argomento il file di destinazione
    print("processing file " + sys.argv[1])
    cap = pyshark.FileCapture(sys.argv[1])

    authorized = False
    headers = {'Content-type': 'application/json', "Accept": "application/json"}

    #apro in scrittura il file di destinazione
    pythonScript = open(sys.argv[2], 'w')
    pythonScript.write("import requests\n")
    pythonScript.write("import json\n")
    pythonScript.write("import time\n")
    pythonScript.write("import re\n\n")

    for packet in cap:
        #print(dir(packet.tcp))
        #print(dir(packet.http))
        print(str(packet.layers))
        print("mongo:"+str(dir(packet.mongo)))
        print("database_name:"+packet.mongo.database_name)
        print("collection_name:" + packet.mongo.collection_name)
        print("addr:"+packet.ip.addr)
        print("src:" + packet.ip.src)
        print("sorgente:"+str(packet.ip.src_host))
        print("destinario:"+str(packet.ip.dst_host))
        if 'IP' in str(packet.layers):
            # print(packet.http)
            if not authorized:
                headers['Authorization'] = packet.http.authorization
                pythonScript.write("headers=" + str(headers) + "\n\n")
                authorized = True

            if str(packet.http.chat).startswith('POST') or str(packet.http.chat).startswith('GET'):
                db_cleanup(packet, pythonScript)
                print("creato......")
                pythonScript.close()
                return

    pythonScript.close()


def db_cleanup(packet, pythonScript):

    """
    prints code which cleans the database up
    :param packet: packet request to replay
    :param pythonScript: script to write the cleanup to
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
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location

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

if __name__ == "__main__":
    main()
