import pyshark
import os
import json
import string
import sys
import re
import subprocess
import json




def main():

    authorized = False
    headers = {'Content-type': 'application/json', "Accept": "application/json"}

    #apro in scrittura il file di destinazione
    pythonScript = open(sys.argv[1], 'w')
    pythonScript.write("import requests\n")
    pythonScript.write("import json\n")
    pythonScript.write("import time\n")
    pythonScript.write("import re\n\n")


    #Devo prendere file report e file monitor e confrontarli usando il campo request_id
    with open(sys.argv[2], 'r') as f:
        array = json.load(f)

    print(array)
    print(array['request_id'])

    data = []
    with open(sys.argv[3], 'r') as f:
        for line in f:
            data.append(json.loads(line))



    print(data[0]['request_id'])

    pythonScript.close()



#     #Pacchetti estratti dal file pcap dove sono memorizzati i pacchetti catturati da un'interfaccia docker
#     for packet in cap:
#         if 'mongo' in str(packet.layers):
#             # print(packet.http)
#             if not authorized:
#                 headers['Authorization'] = packet.http.authorization
#                 pythonScript.write("headers=" + str(headers) + "\n\n")
#                 authorized = True
#                 #Se il file considerato contiene un'operazione
#             if "operation" in sys.argv[1]:
#                 #eseguo operazione contenuta al suo interno
#                 command =
#                 subprocess.Popen("cwm --rdf test.rdf --ntriples > test.nt")
#                 #controllo codice di risposta
#                 #analizzo report per vedere se la risposta è corretta
#
#     pythonScript.close()
#
#
# def write_get_request(packet, pythonScript):
#
#     """
#     writes a get request to a python script
#     :param packet: packet request to replay
#     :param pythonScript: script to write the request to
#     """
#
#     url = 'http://localhost:'
#
#     api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
#     print("------inizio-------")
#     print(api_location)
#     api_location = re.sub(r'\?.*', '/', api_location)
#     print(api_location)
#     print("------fine-------")
#     if not api_location.endswith('/'):
#         api_location += '/'
#     print('get')
#     print(api_location)
#     url = url + re.sub(r'.*:', '', packet.http.host) + api_location
#
#     # hardcoded check, remove
#     if url.__contains__('dialog'):
#         return
#
#     pythonScript.write("print('sending get request to " + url + "')\n")
#     pythonScript.write("response = requests.get('"+url+"', headers=headers)\n")
#     pythonScript.write("print('response: {0}'.format(response.content))\n\n")
#
#
#
# def write_post_request(packet, pythonScript):
#
#     """
#     writes a post request to a python script
#     :param packet: packet request to replay
#     :param pythonScript: script to write the request to
#     """
#
#     url = 'http://localhost:'
#
#     api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
#     print("------inizio-------")
#     print(api_location)
#     api_location = re.sub(r'\?.*', '/', api_location)
#     print(api_location)
#     print("------fine-------")
#     if not api_location.endswith('/'):
#         api_location += '/'
#     print('post')
#     print(api_location)
#     url = url + re.sub(r'.*:', '', packet.http.host) + api_location
#     json_post = packet.http.file_data
#
#     json_post = json_post.replace('null', 'None')
#     pythonScript.write("print('sending post request to "+url+"')\n")
#     pythonScript.write("json_content = "+json_post+"\n")
#     pythonScript.write('print(str(json_content))\n')
#     pythonScript.write("response = requests.post('"+url+"', data=json.dumps(json_content), headers=headers)\n")
#     pythonScript.write("if response.status_code == 201:\n")
#     pythonScript.write("\tprint('created')\n\n")
#
#
# def write_put_request(packet, pythonScript):
#
#     """
#     writes a put request to a python script
#     :param packet: packet request to replay
#     :param pythonScript: script to write the request to
#     """
#
#     url = 'http://localhost:'
#
#     username=packet.http.authbasic.split(':')[0]
#     password=packet.http.authbasic.split(':')[1]
#
#     api_location = re.sub(r'.*\s/', '/', str(packet.http.chat)[:-13])
#     api_location = re.sub(r'\?.*', '/', api_location).split(':')[0]
#     if not api_location.endswith('/'):
#         api_location += '/'
#     print('put')
#     print(api_location)
#     url = url + re.sub(r'.*:', '', packet.http.host) + api_location
#
#     pythonScript.write("print('sending get request to " + url + "')\n")
#     pythonScript.write("response = requests.get('"+url+"', headers=headers, auth=HTTPBasicAuth('"+username+"', '"+password+"'))\n")
#     pythonScript.write("print('response: {0}'.format(response.content))\n\n")
#
#
# def write_assertion(packet, pythonScript):
#
#     """
#     writes an assertion in the replay script to make sure the response to a request is as expected
#     :param packet: the response packet to get the assertion from
#     :param pythonScript: the script to write the assertion to
#     """
#
#
#     if 'file_data' in packet.http.field_names:
#
#         # hardcoded check, remove
#         if re.sub(r'\"id\".*?(?=,)', '\"id\":None', packet.http.file_data).__contains__('<div'):
#             return
#
#         pythonScript.write("assert response.status_code == " + packet.http.chat[9:12] + "\n\n")
#         pythonScript.write("content = re.sub(r'\"id\".*?(?=,)', '\"id\":None',response.content.decode('utf-8'))\n")
#         pythonScript.write("assert content == '" + re.sub(r'\"id\".*?(?=,)', '\"id\":None', packet.http.file_data) + "'\n\n")
#
#
# def db_cleanup(url, pythonScript):
#
#     """
#     prints code which cleans the database up
#     :param url: container url
#     :param pythonScript: script to write the cleanup to
#     """
#
#     pythonScript.write("print('setup: cleaning the database')\n")
#     pythonScript.write("response = requests.get('"+url+"', headers=headers)\n")
#     pythonScript.write("items = json.loads(response.text)\n")
#     pythonScript.write("item_ids = []\n")
#     pythonScript.write("for item in items:\n")
#     pythonScript.write("\turl = '"+url+"/' + str(item['id'])\n")
#     pythonScript.write("\tprint('deleting item ' + str(item['id']))\n")
#     pythonScript.write("\tr = requests.delete(url, data=json.dumps(item_ids), headers=headers)\n")
#     pythonScript.write("\tif r.status_code == 200:\n")
#     pythonScript.write("\t\tprint('ok')\n")
#     pythonScript.write("print('starting replay')\n")


if __name__ == "__main__":
    main()
