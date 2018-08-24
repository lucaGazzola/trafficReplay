import pyshark
import os
import json
import string
import sys
import re
import subprocess
import json

def main():

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
    #print(array['request_id'])


    with open(sys.argv[3], 'r') as test:
        arraytest = json.load(test)

    print(arraytest)

    operation = array['op']
    operation_test = arraytest['op']

    assert operation == operation_test

    print("\n\noperation= "+operation+" optest= "+operation_test+"\n")

    if operation == "insert":
        print("operazione di inserimento")
        req_data = array['request_data']
        req_data_test = arraytest['request_data']
        assert len(req_data) == len(req_data_test)
        doc = req_data['documents']
        doc_test = req_data_test['documents']
        assert len(doc) == len(doc_test)
        for i in range(0,len(doc)):
            assert len(doc[i]) == len(doc_test[i])
            for key, value in doc[i].items():
                if key != "_class" and key != "_id":
                    assert doc[i][key] == doc_test[i][key]
        ins = req_data['insert']
        ins_test = req_data_test['insert']
        assert ins == ins_test
        order = req_data['ordered']
        order_test = req_data_test['ordered']
        assert order == order_test
        rep_data = array['reply_data']
        rep_data_test = arraytest['reply_data']
        assert len(rep_data) == len(rep_data_test)
        n = rep_data['n']
        n_test = rep_data_test['n']
        assert n == n_test
        ok = rep_data['ok']
        ok_test = rep_data_test['ok']
        assert ok == ok_test
        pythonScript.close()
        return

    if operation == "update":
        print("operazione di aggiornamento")
        req_data = array['request_data']
        req_data_test = arraytest['request_data']
        assert len(req_data) == len(req_data_test)
        up = req_data['update']
        up_test = req_data_test['update']
        assert up == up_test
        order = req_data['ordered']
        order_test = req_data_test['ordered']
        assert order == order_test
        updates = req_data['updates']
        updates_test = req_data_test['updates']
        assert len(updates) == len(updates_test)
        for i in range(0, len(updates)):
            assert len(updates[i]) == len(updates_test[i])
            for key, value in updates[i].items():
                #q contiene id dell'eliminato , u contiene i dati del nuovo
                if key != "u" and key != "_id" and key != 'q':
                    assert updates[i][key] == updates_test[i][key]
                if key == 'u':
                    for keys, values in updates[i][key].items():
                        if keys != "_class" and keys != "_id":
                            assert updates[i][key][keys] == updates_test[i][key][keys]
        rep_data = array['reply_data']
        rep_data_test = arraytest['reply_data']
        assert len(rep_data) == len(rep_data_test)
        n = rep_data['n']
        n_test = rep_data_test['n']
        assert n == n_test
        ok = rep_data['ok']
        ok_test = rep_data_test['ok']
        assert ok == ok_test
        modif = rep_data['nModified']
        modif_test = rep_data_test['nModified']
        assert modif == modif_test
        pythonScript.close()
        return

    if operation == "delete":
        print("operazione di delete")
        req_data = array['request_data']
        req_data_test = arraytest['request_data']
        assert len(req_data) == len(req_data_test)
        delete = req_data['delete']
        delete_test = req_data_test['delete']
        assert delete == delete_test
        order = req_data['ordered']
        order_test = req_data_test['ordered']
        assert order == order_test
        deletes = req_data['deletes']
        deletes_test = req_data_test['deletes']
        assert len(deletes) == len(deletes_test)
        for i in range(0, len(deletes)):
            assert len(deletes[i]) == len(deletes_test[i])
            for key, value in deletes[i].items():
                if key == 'q':
                    for keys, values in deletes[i][key].items():
                        assert deletes[i][key][keys]['$oid'] == deletes_test[i][key][keys]['$oid']
                else:
                    assert deletes[i][key] == deletes_test[i][key]
        rep_data = array['reply_data']
        rep_data_test = arraytest['reply_data']
        assert len(rep_data) == len(rep_data_test)
        n = rep_data['n']
        n_test = rep_data_test['n']
        assert n == n_test
        ok = rep_data['ok']
        ok_test = rep_data_test['ok']
        assert ok == ok_test
        pythonScript.close()
        return

    if operation == "command":
        operation = array['command']
        operation_test = arraytest['command']
        print("\n\noperation= " + operation + " optest= " + operation_test + "\n")
        assert operation == operation_test
        print("operazione di ricerca")
        req_data = array['request_data']
        req_data_test = arraytest['request_data']
        assert len(req_data) == len(req_data_test)
        filt = req_data['filter']
        filt_test = req_data_test['filter']
        assert filt ==filt_test
        find = req_data['find']
        find_test = req_data_test['find']
        assert find == find_test
        limit = req_data['limit']
        limit_test = req_data_test['limit']
        assert limit == limit_test
        rep_data = array['reply_data']
        rep_data_test = arraytest['reply_data']
        assert len(rep_data) == len(rep_data_test)
        cursor = rep_data['cursor']
        cursor_test = rep_data_test['cursor']
        assert len(cursor) == len(cursor_test)
        for key, value in cursor.items():
            if key == "firstBatch":
                assert len(cursor[key]) == len(cursor_test[key])
                for i in range(0, len(cursor[key])):
                    for keys, values in cursor[key][i].items():
                        if keys != "_class" and keys != "_id":
                            assert  cursor[key][i][keys] == cursor_test[key][i][keys]
        pythonScript.close()
        return


    pythonScript.close()






if __name__ == "__main__":
    main()
