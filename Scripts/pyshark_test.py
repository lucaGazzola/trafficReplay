import pyshark
import os
import json
import string
import sys
import re
from bson.json_util import loads



def main():

    # 1st argument: name of pcap file
    # 2nd argument: generated python test script name
    # 3rd argument: list of ips of applications under test

    """
    creates a script that replays an interaction with a docker container in a microservice application
    """
    cap = pyshark.FileCapture(sys.argv[1])

    pythonScript = None

    controllo = True

    port_list = sys.argv[3].split(',')

    headers = {'Content-type': 'application/json', "Accept": "application/json"}

    # Packets extracted from pcap file
    for packet in cap:
        # For each ip
        for port in port_list:

        # REST -> quindi vado a considerare protocollo ad alto livello
        # Questa parte deve essere modificata una volta presente la parte di mockup dei microservizi che sostituiscono
        # gli altri microservizi che comunicano con il microservizio che stiamo testando
        # Questa parte è diversa per ogni microservizio testato in quanto dipende dal tipo di configurazione richiesta e
        # dal tipo di autenticazione implementata
        # In questo caso (PiggyMetrics) abbiamo comunicazione con microservizio auth che ci fornisce token per servizo
        # authentication o per singolo utente registrato



            # Check from ip list
            if 'HTTP' in str(packet.layers) and 'TCP' in str(packet.layers) and ( packet.tcp.srcport == port or packet.tcp.dstport == port ):

                # Open dst file
                if pythonScript is None or pythonScript.closed:
                    pythonScript = open(sys.argv[2], 'w')

                if str(packet.http.chat).startswith('POST'):
                    if not controllo:
                        pythonScript.write("try:\n")
                        pythonScript.write("\tassert response.status_code == 200\n")
                        pythonScript.write("except AssertionError:\n")
                        pythonScript.write("\tcodeexit=1\n")
                        pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                        pythonScript.write("\tlogging.debug(' codice status ricevuto: '+str(response.status_code))\n")
                        pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                        pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
                    pythonScript.write("headers=" + str(headers) + "\n\n")
                    write_post_request(packet, pythonScript)
                    controllo = False

                if str(packet.http.chat).startswith('GET'):
                    if not controllo:
                        pythonScript.write("try:\n")
                        pythonScript.write("\tassert response.status_code == 200\n")
                        pythonScript.write("except AssertionError:\n")
                        pythonScript.write("\tcodeexit=1\n")
                        pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                        pythonScript.write("\tlogging.debug(' codice status ricevuto: '+str(response.status_code))\n")
                        pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                        pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
                    write_get_request(packet, pythonScript, headers)
                    controllo = False

                if str(packet.http.chat).startswith('PUT'):
                    if not controllo:
                        pythonScript.write("try:\n")
                        pythonScript.write("\tassert response.status_code == 200\n")
                        pythonScript.write("except AssertionError:\n")
                        pythonScript.write("\tcodeexit=1\n")
                        pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                        pythonScript.write("\tlogging.debug(' codice status ricevuto: '+str(response.status_code))\n")
                        pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                        pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
                    write_put_request(packet, pythonScript, headers)
                    controllo = False

                if str(packet.http.chat).startswith('DELETE'):
                    if not controllo:
                        pythonScript.write("try:\n")
                        pythonScript.write("\tassert response.status_code == 200\n")
                        pythonScript.write("except AssertionError:\n")
                        pythonScript.write("\tcodeexit=1\n")
                        pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                        pythonScript.write("\tlogging.debug(' codice status ricevuto: '+str(response.status_code))\n")
                        pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                        pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
                    pythonScript.write("headers=" + str(headers) + "\n\n")
                    write_delete_request(packet, pythonScript)
                    controllo = False

                if str(packet.http.chat).startswith('HTTP'):
                    write_assertion(packet, pythonScript)
                    controllo = True #Se controllo è True significa che ho messo condizione di controllo

    if not pythonScript is None:
        pythonScript.close()


def write_import(pythonScript):
    pythonScript.write("import requests\n")
    pythonScript.write("import json\n")
    pythonScript.write("import time\n")
    pythonScript.write("import re\n")
    pythonScript.write("import sys\n")
    pythonScript.write("from bson.json_util import loads \n")
    pythonScript.write("import os.path\n\n")


# #richiesta token applicazione --> usata quando voglio dati di un singolo utente (specificato in uri)
# def get_token_appl(pythonScript,id,passw):
#     """
#     writes a get request to a python script
#     :param pythonScript: script to write the request to
#     :param id: application id
#     :param passw: application password
#
#     """
#
#     pythonScript.write("data = {'grant_type': 'client_credentials'}\n")
#     pythonScript.write("token_appl = requests.post('http://localhost:5000/uaa/oauth/token', headers=headers, data=data, auth=('"+str(id)+"', '"+str(passw)+"'))\n")
#
# #richiesta token singolo utente ---> usata per richiesta dati utente corrente
# def get_token_user(pythonScript):
#     """
#     writes a get request to a python script
#     :param pythonScript: script to write the request to
#
#     """
#
#     pythonScript.write("headers = { 'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic YnJvd3Nlcjo=' }\n")
#     "scope=ui&grant_type=password&username=" + str(username) + "&password=" + str(password)
#
#
#     pythonScript.write("data = 'scope=ui&grant_type=password&username='+str(username)+'&password='+str(password)\n")
#     pythonScript.write("token_user = requests.post('http://localhost:5000/uaa/oauth/token', headers=headers, data=data)\n")
#     pythonScript.write("token_string = token_user.content.decode('utf-8')\n")
#     pythonScript.write("token_json = json.loads(token_string)\n")
#     pythonScript.write("token = 'Bearer ' + str(token_json['access_token'])\n")



def write_get_request(packet, pythonScript, headers):

    """
    writes a get request to a python script
    :param packet: packet request to replay
    :param pythonScript: script to write the request to
    """
    url = "http://localhost:"

    api_location = str(packet.http.chat).split(" ")[1]
    api_location = re.sub(r'\?.*', '/', api_location)
    # if not api_location.endswith('/'):
    #     api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location

    # hardcoded check, remove
    if url.__contains__('dialog'):
        return

    #print(packet.http.field_names)

    if 'authorization' in packet.http.field_names:
        headers['Authorization'] = packet.http.authorization

    pythonScript.write("headers=" + str(headers) + "\n\n")

    #
    # #Posso mettere un qualsiasi token di autorizzazione visto che al posto dell'applicazione che fa il controllo metto il mio mockup
    # pythonScript.write("headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer b52d8972-f588-4a98-86e0-65272cda65af'}\n\n")
    # # Se l'url termina con /current si sta facendo riferimento al profilo corrente quindi serve token di autenticazione dell'utente
    # last_part = url.rsplit('/', 1)[-1]
    # if last_part == "current":
    # #     get_token_user(pythonScript)
    #     pythonScript.write("headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer b52d8972-f588-4a98-86e0-65272cda65af'}\n\n")
    # #Altrimenti serve token dell'applicazione perchè sto richiedendo per un utente in particolare
    # else:
    # #     get_token_appl(pythonScript, "account-service", passw)
    # #     pythonScript.write("token = \"Bearer \"+str(token_appl)\n")
    #     pythonScript.write("headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer 1b4270ff-d035-4d17-a2ff-9b350dea66be'}\n\n")

    pythonScript.write("print('sending get request to " + url + "')\n")
    pythonScript.write("response = requests.get('"+url+"', headers=headers)\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n\n")



def write_post_request(packet, pythonScript):

    """
    writes a post request to a python script
    :param packet: packet request to replay
    :param pythonScript: script to write the request to
    """

    url = "http://localhost:"

    api_location = str(packet.http.chat).split(" ")[1]
    api_location = re.sub(r'\?.*', '/', api_location)
    # if not api_location.endswith('/'):
    #     api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location
    json_post = packet.http.file_data

    json_post = json_post.replace('null', 'None')
    pythonScript.write("print('sending post request to "+url+"')\n")
    pythonScript.write("json_content = "+json_post+"\n")
    pythonScript.write("response = requests.post('"+url+"', data=json.dumps(json_content), headers=headers)\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n")
    pythonScript.write("if response.status_code == 201:\n")
    pythonScript.write("\tprint('created')\n\n")

    #pythonScript.write("username = json_content['username']\n")
    #pythonScript.write("password = json_content['password']\n\n")


def write_put_request(packet, pythonScript, headers):

    """
    writes a put request to a python script
    :param packet: packet request to replay
    :param pythonScript: script to write the request to
    """

    url = "http://localhost:"


    api_location = str(packet.http.chat).split(" ")[1]
    api_location = re.sub(r'\?.*', '/', api_location).split(':')[0]
    # if not api_location.endswith('/'):
    #     api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location

    if 'authorization' in packet.http.field_names:
        headers['Authorization'] = packet.http.authorization

    pythonScript.write("headers=" + str(headers) + "\n\n")

    #pythonScript.write("headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer b52d8972-f588-4a98-86e0-65272cda65af'}\n\n")
    # Se l'url termina con /current si sta facendo riferimento al profilo corrente quindi serve token di autenticazione dell'utente
    # last_part = url.rsplit('/', 1)[-1]
    # if last_part == "current":
    #     get_token_user(pythonScript)
    #     pythonScript.write("headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': token}\n\n")
    #     #pythonScript.write("headers=('Accept': 'application/json', 'Authorization': token  )\n\n")


    pythonScript.write("data = {}\n")
    if 'file_data' in packet.http.field_names:
        #print(packet.http.field_names)
        packet.http.file_data = packet.http.file_data.replace("'", '\\\'')
        pythonScript.write("data = json.loads('"+packet.http.file_data+"')\n")
    pythonScript.write("print('sending put request to " + url + "')\n")
    pythonScript.write("response = requests.put('"+url+"', data = json.dumps(data), headers=headers)\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n\n")




def write_delete_request(packet, pythonScript):

    """
        writes a delete request to a python script
        :param packet: packet request to replay
        :param pythonScript: script to write the request to
    """

    url = "http://localhost:"

    api_location = str(packet.http.chat).split(" ")[1]
    api_location = re.sub(r'\?.*', '/', api_location).split(':')[0]
    # if not api_location.endswith('/'):
    #     api_location += '/'
    url = url + re.sub(r'.*:', '', packet.http.host) + api_location
    pythonScript.write("url = '" + url + "'\n")
    pythonScript.write("print('sending delete request to '+ url)\n")
    pythonScript.write("response = requests.delete(url, headers=headers)\n")
    pythonScript.write("print('response: {0}'.format(response.content))\n\n")
    pythonScript.write("assert response.status_code == 200\n\n")



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

        if 'response_phrase' in packet.http.field_names and packet.http.response_phrase == "Created":
            pythonScript.write("cont = loads(response.content.decode('utf-8'))\n")
        #Viene fatta la redirect
        if packet.http.chat[9:12] == '302':
            packet.http.location = packet.http.location.rsplit(':', 1)[-1]
            addr = "http://localhost:"+str(packet.http.location)
            pythonScript.write("response2 = requests.get('"+str(addr)+"', headers=headers)\n")
            #pythonScript.write("assert response.status_code == response2.status_code\n\n")
            pythonScript.write("try:\n")
            pythonScript.write("\tassert response.status_code == response2.status_code\n")
            pythonScript.write("except AssertionError:\n")
            pythonScript.write("\tcodeexit=1\n")
            pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
            pythonScript.write("\tlogging.debug(' codice status ricevuto:'+str(response.status_code))\n")
            pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
            pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
            pythonScript.write("\tlogging.debug(' codice status2 ricevuto:'+str(response2.status_code ))\n")
            pythonScript.write("\tcontent2 = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response2.content.decode('utf-8'))\n")
            pythonScript.write("\tlogging.debug(' contenuto pacchetto2: '+str(content2))\n\n")
        else:
            if ("http://statistics-service/statistics" not in str(packet.http.file_data)) and ("updateStatistics(String,Account)" not in str(packet.http.file_data)):
                pythonScript.write("try:\n")
                pythonScript.write("\tassert response.status_code == " + packet.http.chat[9:12] + "\n")
                pythonScript.write("except AssertionError:\n")
                pythonScript.write("\tcodeexit=1\n")
                pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                pythonScript.write("\tlogging.debug(' codice status ricevuto: '+str(response.status_code))\n")
                pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
                pythonScript.write("\tlogging.debug(' contenuto che doveva avere il pacchetto:" + str(packet.http.file_data).replace("'","\\'") + "')\n\n")
                #pythonScript.write("assert response.status_code == " + packet.http.chat[9:12] + "\n\n")
                pythonScript.write("content = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                pythonScript.write("content = re.sub(r'\"timestamp\".*?(?=,)', '\"timestamp\":null',content)\n")
                pythonScript.write("content = re.sub(r'\"lastSeen\".*?(?=,)', '\"lastSeen\":null',content)\n")
                pythonScript.write("content = re.sub(r'\"date\".*?(?=,)', '\"date\":null',content)\n")
                pythonScript.write("content = content.replace('\\n', '')\n")
                pythonScript.write("data_cont = loads(content)\n")
                #pythonScript.write("if 'path' in data_cont and data_cont['path'].endswith('/'):\n")
                #pythonScript.write("\tdata_cont['path'] = data_cont['path'][:-1]\n")
                packet.http.file_data = packet.http.file_data.replace("'", '\\\'')
                pythonScript.write("packet_data = '" + re.sub(r'\"id\".*?(?=,)', '\"id\":null', packet.http.file_data) + "'\n")
                pythonScript.write("packet_data = re.sub(r'\"timestamp\".*?(?=,)', '\"timestamp\":null', packet_data)\n")
                pythonScript.write("packet_data = re.sub(r'\"lastSeen\".*?(?=,)', '\"lastSeen\":null', packet_data)\n")
                pythonScript.write("packet_data = re.sub(r'\"date\".*?(?=,)', '\"date\":null', packet_data)\n")
                pythonScript.write("packet_data = packet_data.replace('\\n', '')\n")
                pythonScript.write("packet_data = packet_data.replace('\">','').replace('\"-','')\n")
                pythonScript.write("print(packet_data)\n")
                pythonScript.write("data_pkt = loads(packet_data)\n")
                pythonScript.write("try:\n")
                pythonScript.write("\tassert data_cont == data_pkt\n")
                pythonScript.write("except AssertionError:\n")
                pythonScript.write("\tcodeexit=1\n")
                pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                pythonScript.write("\tlogging.debug(str(traceback.print_exc()))\n")
                pythonScript.write("\tlogging.debug('contenuto pacchetto:'+str(data_cont))\n")
                pythonScript.write("\tlogging.debug('contenuto che doveva avere pacchetto:'+str(data_pkt))\n\n")


    else:
        #Quando arriva pacchetto con codice 100 è perchè deve ancora arrivare l'ultima parte del messaggio
            #Quindi salto questo pacchetto e aspetto il completamento
        if 'chat' in packet.http.field_names and not(packet.http.chat[9:12] == '100'):
            if packet.http.chat[9:12] == 302:
                pythonScript.write("response2 = requests.get('"+str(addr)+"', headers=headers)\n")
                pythonScript.write("try:\n")
                pythonScript.write("\tassert response.status_code == response2.status_code\n")
                pythonScript.write("except AssertionError:\n")
                pythonScript.write("\tcodeexit=1\n")
                pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                pythonScript.write("\tlogging.debug(str(traceback.print_exc()))\n")
                pythonScript.write("\tlogging.debug(' codice status ricevuto:'+str(response.status_code))\n")
                pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
                pythonScript.write("\tlogging.debug(' codice status2 ricevuto:'+str(response2.status_code ))\n")
                pythonScript.write("\tcontent2 = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response2.content.decode('utf-8'))\n")
                pythonScript.write("\tlogging.debug(' contenuto pacchetto2: '+str(content2))\n\n")
            else:
                #pythonScript.write("assert response.status_code == " + packet.http.chat[9:12] + "\n\n")
                pythonScript.write("try:\n")
                pythonScript.write("\tassert response.status_code == " + packet.http.chat[9:12] + "\n")
                pythonScript.write("except AssertionError:\n")
                pythonScript.write("\tcodeexit=1\n")
                pythonScript.write("\tlogging.exception(str(traceback.print_exc()))\n")
                pythonScript.write("\tlogging.debug(' codice status ricevuto: '+str(response.status_code))\n")
                pythonScript.write("\tcontent = re.sub(r'\"id\".*?(?=,)', '\"id\":null',response.content.decode('utf-8'))\n")
                pythonScript.write("\tlogging.debug(' contenuto pacchetto: '+str(content))\n")
        #pythonScript.write("assert str(response) == \"<Response [200]>\" \n\n")


if __name__ == "__main__":
    main()
