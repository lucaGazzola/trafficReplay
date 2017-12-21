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

    print("processing file " + sys.argv[1])
    cap = pyshark.FileCapture(sys.argv[1])

    authorized = False
    headers = {'Content-type': 'application/json', "Accept": "application/json"}

    pythonScript = open(sys.argv[2], 'w')
    pythonScript.write("import requests\n")
    pythonScript.write("import json\n")
    pythonScript.write("import time\n")
    pythonScript.write("import re\n\n")

    for packet in cap:
        if 'HTTP' in str(packet.layers):
            # print(packet.http)
            if not authorized:
                headers['Authorization'] = packet.http.authorization
                pythonScript.write("headers=" + str(headers) + "\n\n")
                authorized = True

            if str(packet.http.chat).startswith('POST'):
                write_post_request(packet, pythonScript)

            if str(packet.http.chat).startswith('GET'):
                write_get_request(packet, pythonScript)

            if str(packet.http.chat).startswith('PUT'):
                # print(packet.http._all_fields)
                write_put_request(packet, pythonScript)

            if str(packet.http.chat).startswith('HTTP'):
                write_assertion(packet, pythonScript)

    pythonScript.close()


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
    print('get')
    print(api_location)
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location

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

    pythonScript.write("assert response.status_code == " + packet.http.chat[9:12] + "\n\n")
    if 'file_data' in packet.http.field_names:
        pythonScript.write("content = re.sub(r'\"id\".*?(?=,)', '\"id\":None',str(response.content))\n")
        pythonScript.write("assert content[2:-1] == '" + re.sub(r'\"id\".*?(?=,)', '\"id\":None', packet.http.file_data) + "'\n\n")


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
