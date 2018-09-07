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
        pythonScript.write("req_data = " + str(array['request_data']) + "\n")
        req_data_test = arraytest['request_data']
        pythonScript.write("print('assert: number of request data')\n")
        pythonScript.write("assert len(req_data)  == " + str(len(req_data_test)) + "\n\n")

        pythonScript.write("doc = " + str(req_data['documents']) + "\n")
        pythonScript.write("doc_test = " + str(req_data_test['documents']) + "\n")
        pythonScript.write("print('assert: number of document elements')\n")
        pythonScript.write("assert len(doc) == len(doc_test)\n\n")

        pythonScript.write("for i in range(0, len(doc)):\n")
        pythonScript.write("\tassert len(doc[i]) == len(doc_test[i])\n")
        pythonScript.write("\tfor key, value in doc[i].items():\n")
        pythonScript.write("\t\tif key != '_class' and key != '_id':\n")
        pythonScript.write("\t\t\tassert doc[i][key] == doc_test[i][key]\n")

        pythonScript.write("\nins = '" + req_data['insert'] + "'\n")
        ins_test = req_data_test['insert']
        pythonScript.write("print('assert: insert elements')\n")
        pythonScript.write("assert ins  == '" + ins_test + "'\n\n")

        pythonScript.write("order = " + str(req_data['ordered']) + "\n")
        order_test = req_data_test['ordered']
        pythonScript.write("print('assert: order elements')\n")
        pythonScript.write("assert order  == " + str(order_test) + "\n\n")

        rep_data = array['reply_data']
        pythonScript.write("rep_data = " + str(array['reply_data']) + "\n")
        rep_data_test = arraytest['reply_data']
        pythonScript.write("print('assert: number of reply data')\n")
        pythonScript.write("assert len(rep_data)  == " + str(len(rep_data_test)) + "\n\n")

        pythonScript.write("n = " + str(rep_data['n']) + "\n")
        n_test = rep_data_test['n']
        pythonScript.write("print('assert: n elements')\n")
        pythonScript.write("assert n  == " + str(n_test) + "\n\n")

        pythonScript.write("ok = " + str(rep_data['ok']) + "\n")
        ok_test = rep_data_test['ok']
        pythonScript.write("print('assert: ok elements')\n")
        pythonScript.write("assert ok  == " + str(ok_test) + "\n\n")

        pythonScript.close()
        return

    if operation == "update":
        print("operazione di aggiornamento")

        req_data = array['request_data']
        pythonScript.write("req_data = " + str(array['request_data']) + "\n")
        req_data_test = arraytest['request_data']
        pythonScript.write("print('assert: number of request data')\n")
        pythonScript.write("assert len(req_data)  == " + str(len(req_data_test)) + "\n\n")

        pythonScript.write("up = '" + req_data['update'] + "'\n")
        up_test = req_data_test['update']
        pythonScript.write("print('assert: update elements')\n")
        pythonScript.write("assert up == '" + up_test + "'\n\n")

        pythonScript.write("order = " + str(req_data['ordered']) + "\n")
        order_test = req_data_test['ordered']
        pythonScript.write("print('assert: ordered elements')\n")
        pythonScript.write("assert order == " + str(order_test) + "\n\n")

        pythonScript.write("updates = " + str(req_data['updates']) + "\n")
        pythonScript.write("updates_test = " + str(req_data_test['updates']) + "\n")
        pythonScript.write("print('assert: number of updates elements')\n")
        pythonScript.write("assert len(updates) == len(updates_test)\n\n")

        pythonScript.write("for i in range(0, len(updates)):\n")
        pythonScript.write("\tassert len(updates[i]) == len(updates_test[i])\n")
        pythonScript.write("\tfor key, value in updates[i].items():\n")
        pythonScript.write("\t\tif key != 'u' and key != '_id' and key != 'q':\n")
        pythonScript.write("\t\t\tassert updates[i][key] == updates_test[i][key]\n")
        pythonScript.write("\t\tif key == 'u':\n")
        pythonScript.write("\t\t\tfor keys, values in updates[i][key].items():\n")
        pythonScript.write("\t\t\t\tif keys != '_class' and keys != '_id':\n")
        pythonScript.write("\t\t\t\t\t assert updates[i][key][keys] == updates_test[i][key][keys]\n")

        rep_data = array['reply_data']
        pythonScript.write("\nrep_data = " + str(array['reply_data']) + "\n")
        rep_data_test = arraytest['reply_data']
        pythonScript.write("print('assert: number of reply data')\n")
        pythonScript.write("assert len(rep_data) == " + str(len(rep_data_test)) + "\n\n")

        pythonScript.write("n = " + str(rep_data['n']) + "\n")
        n_test = rep_data_test['n']
        pythonScript.write("print('assert: n elements')\n")
        pythonScript.write("assert n  == " + str(n_test) + "\n\n")

        pythonScript.write("ok = " + str(rep_data['ok']) + "\n")
        ok_test = rep_data_test['ok']
        pythonScript.write("print('assert: ok elements')\n")
        pythonScript.write("assert ok  == " + str(ok_test) + "\n\n")

        pythonScript.write("modif = " + str(rep_data['nModified']) + "\n")
        modif_test = rep_data_test['nModified']
        pythonScript.write("print('assert: nModified elements')\n")
        pythonScript.write("assert modif  == " + str(modif_test) + "\n\n")


        pythonScript.close()
        return

    if operation == "delete":
        print("operazione di delete")

        req_data = array['request_data']
        pythonScript.write("req_data = " + str(array['request_data']) + "\n")
        req_data_test = arraytest['request_data']
        pythonScript.write("print('assert: number of request data')\n")
        pythonScript.write("assert len(req_data)  == " + str(len(req_data_test)) + "\n\n")

        pythonScript.write("delete = '" + req_data['delete'] + "'\n")
        delete_test = req_data_test['delete']
        pythonScript.write("print('assert: delete elements')\n")
        pythonScript.write("assert delete == '" + delete_test + "'\n\n")

        pythonScript.write("order = " + str(req_data['ordered']) + "\n")
        order_test = req_data_test['ordered']
        pythonScript.write("print('assert: ordered elements')\n")
        pythonScript.write("assert order == " + str(order_test) + "\n\n")

        pythonScript.write("deletes = " + str(req_data['deletes']) + "\n")
        pythonScript.write("deletes_test = " + str(req_data_test['deletes']) + "\n")
        pythonScript.write("print('assert: number of deletes elements')\n")
        pythonScript.write("assert len(deletes) == len(deletes_test) \n\n")

        pythonScript.write("for i in range(0, len(deletes)):\n")
        pythonScript.write("\tassert len(deletes[i]) == len(deletes_test[i])\n")
        pythonScript.write("\tfor key, value in deletes[i].items():\n")
        pythonScript.write("\t\tif key == 'q':\n")
        pythonScript.write("\t\t\tfor keys, values in deletes[i][key].items():\n")
        pythonScript.write("\t\t\t\tassert deletes[i][key][keys]['$oid'] == deletes_test[i][key][keys]['$oid']\n")
        pythonScript.write("\t\telse:\n")
        pythonScript.write("\t\t\tassert deletes[i][key] == deletes_test[i][key]\n")

        rep_data = array['reply_data']
        pythonScript.write("\nrep_data = " + str(array['reply_data']) + "\n")
        rep_data_test = arraytest['reply_data']
        pythonScript.write("print('assert: number of reply data')\n")
        pythonScript.write("assert len(rep_data) == " + str(len(rep_data_test)) + "\n\n")

        pythonScript.write("n = " + str(rep_data['n']) + "\n")
        n_test = rep_data_test['n']
        pythonScript.write("print('assert: n elements')\n")
        pythonScript.write("assert n  == " + str(n_test) + "\n\n")

        pythonScript.write("ok = " + str(rep_data['ok']) + "\n")
        ok_test = rep_data_test['ok']
        pythonScript.write("print('assert: ok elements')\n")
        pythonScript.write("assert ok  == " + str(ok_test) + "\n\n")

        pythonScript.close()
        return

    if operation == "command":
        operation = array['command']
        operation_test = arraytest['command']
        print("\n\noperation= " + operation + " optest= " + operation_test + "\n")
        assert operation == operation_test
        print("operazione di ricerca")

        req_data = array['request_data']
        pythonScript.write("req_data = " + str(array['request_data']) + "\n")
        req_data_test = arraytest['request_data']
        pythonScript.write("print('assert: number of request data')\n")
        pythonScript.write("assert len(req_data)  == " + str(len(req_data_test)) + "\n\n")

        pythonScript.write("filt = " + str(req_data['filter']) + "\n")
        filt_test = req_data_test['filter']
        pythonScript.write("print('assert: filter elements')\n")
        pythonScript.write("assert filt  == " + str(filt_test) + "\n\n")

        pythonScript.write("find = '" + req_data['find'] + "'\n")
        find_test = req_data_test['find']
        pythonScript.write("print('assert: find elements')\n")
        pythonScript.write("assert find  == '" + find_test + "'\n\n")

        pythonScript.write("limit = " + str(req_data['limit']) + "\n")
        limit_test = req_data_test['limit']
        pythonScript.write("print('assert: limit elements')\n")
        pythonScript.write("assert limit == " + str(limit_test) + "\n\n")

        rep_data = array['reply_data']
        pythonScript.write("rep_data = " + str(array['reply_data']) + "\n")
        rep_data_test = arraytest['reply_data']
        pythonScript.write("print('assert: number of reply data')\n")
        pythonScript.write("assert len(rep_data) == " + str(len(rep_data_test)) + "\n\n")

        pythonScript.write("cursor = " + str(rep_data['cursor']) + "\n")
        pythonScript.write("cursor_test = " + str(rep_data_test['cursor']) + "\n")
        pythonScript.write("print('assert: number of cursor data')\n")
        pythonScript.write("assert len(cursor) == len(cursor_test) \n\n")


        pythonScript.write("for key, value in cursor.items():\n")
        pythonScript.write("\tif key == 'firstBatch':\n")
        pythonScript.write("\t\tassert len(cursor[key])  == len(cursor_test[key]) \n")
        pythonScript.write("\t\tfor i in range(0, len(cursor[key])):\n")
        pythonScript.write("\t\t\tfor keys, values in cursor[key][i].items():\n")
        pythonScript.write("\t\t\t\tif keys != '_class' and keys != '_id':\n")
        pythonScript.write("\t\t\t\t\tassert cursor[key][i][keys] ==  cursor_test[key][i][keys] \n")
        pythonScript.close()
        return


    pythonScript.close()






if __name__ == "__main__":
    main()
