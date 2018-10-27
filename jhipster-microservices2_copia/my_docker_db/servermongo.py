from mockupdb import *
import sys
import json
import pprint
from bson.int64 import Int64
import time
from os import listdir
from os.path import isfile, join



def main():
	print("Attivazione Server....")
	server = MockupDB(port='37379')
	#server = MockupDB()
	#server.address_string(37379)
	port = server.run()
	print(server.uri)
	print(server.address)

	onlyfiles = [f for f in listdir("MockupFolder") if isfile(join("MockupFolder", f))]
	print(onlyfiles)


	ismaster_reply = OpReply({
		"allocator": "tcmalloc",
		"bits": 64,
		"buildEnvironment": {"cc": "/opt/mongodbtoolchain/v2/bin/gcc: gcc (GCC) 5.4.0",
							  "ccflags": "-fno-omit-frame-pointer -fno-strict-aliasing -ggdb -pthread -Wall -Wsign-compare -Wno-unknown-pragmas -Winvalid-pch -Werror -O2 -Wno-unused-local-typedefs -Wno-unused-function -Wno-deprecated-declarations -Wno-unused-but-set-variable -Wno-missing-braces -fstack-protector-strong -fno-builtin-memcmp",
							  "cxx": "/opt/mongodbtoolchain/v2/bin/g++: g++ (GCC) 5.4.0",
							  "cxxflags": "-Woverloaded-virtual -Wno-maybe-uninitialized -std=c++11",
							  "distarch": "x86_64", "distmod": "debian81",
							  "linkflags": "-pthread -Wl,-z,now -rdynamic -Wl,--fatal-warnings -fstack-protector-strong -fuse-ld=gold -Wl,--build-id -Wl,-z,noexecstack -Wl,--warn-execstack -Wl,-z,relro",
							  "target_arch": "x86_64",
							  "target_os": "linux"},
		"debug": False,
		"gitVersion": "078f28920cb24de0dd479b5ea6c66c644f6326e9",
		"javascriptEngine": "mozjs",
		"maxBsonObjectSize": 16777216,
		"modules": [],
		"ok": 1.0,
		"openssl": {"compiled": "OpenSSL 1.0.1t  3 May 2016",
					"running": "OpenSSL 1.0.1t  3 May 2016"},
		"storageEngines": ["devnull", "ephemeralForTest", "mmapv1", "wiredTiger"],
		"sysInfo": "deprecated",
		"version": "3.4.10",
		"versionArray": [3, 4, 10, 0]
	})
	server.autoresponds('ismaster', ismaster_reply)
	server.autoresponds('ping')
	buildinfo_reply = OpReply({
	"allocator":"tcmalloc",
	"bits":64,
	"buildEnvironment":{"cc":"/opt/mongodbtoolchain/v2/bin/gcc: gcc (GCC) 5.4.0",
			"ccflags":"-fno-omit-frame-pointer -fno-strict-aliasing -ggdb -pthread -Wall -Wsign-compare -Wno-unknown-pragmas -Winvalid-pch -Werror -O2 -Wno-unused-local-typedefs -Wno-unused-function -Wno-deprecated-declarations -Wno-unused-but-set-variable -Wno-missing-braces -fstack-protector-strong -fno-builtin-memcmp",
			"cxx":"/opt/mongodbtoolchain/v2/bin/g++: g++ (GCC) 5.4.0",
			"cxxflags":"-Woverloaded-virtual -Wno-maybe-uninitialized -std=c++11",
			"distarch":"x86_64",
			"distmod":"debian81",
			"linkflags":"-pthread -Wl,-z,now -rdynamic -Wl,--fatal-warnings -fstack-protector-strong -fuse-ld=gold -Wl,--build-id -Wl,-z,noexecstack -Wl,--warn-execstack -Wl,-z,relro",
			"target_arch":"x86_64",
			"target_os":"linux"},
	"debug":False,
	"gitVersion":"078f28920cb24de0dd479b5ea6c66c644f6326e9",
	"javascriptEngine":"mozjs",
	"maxBsonObjectSize":16777216,
	"modules":[],
	"ok":1.0,
	"openssl":{"compiled":"OpenSSL 1.0.1t  3 May 2016",
		"running":"OpenSSL 1.0.1t  3 May 2016"},
	"storageEngines":["devnull","ephemeralForTest","mmapv1","wiredTiger"],
	"sysInfo":"deprecated",
	"version":"3.4.10",
	"versionArray":[3,4,10,0]
	})
	server.autoresponds('buildInfo', buildinfo_reply)
	server.autoresponds('buildinfo', buildinfo_reply)
	getlasterror_reply = OpReply({
	"connectionId":4,
	"err":None,
	"n":0,
	"ok":1.0,
	"syncMillis":0,
	"writtenTo":None
	})
	responder = server.autoresponds('getlasterror', getlasterror_reply)
	print(responder)
	#server.pop('buildinfo').ok()
	#responder = server.autoresponds(OpMsg('find', 'collection'),{'cursor': {'id': 0, 'firstBatch': [{'a': 1}, {'a': 2}]}})
	find_reply = OpReply({
		"cursor": {"firstBatch": [], "id": {"$numberLong": "0"},
				   "ns": "db.system.indexes"},
		"ok": 1.0
	})
	server.autoresponds(OpMsg('find', 'collection'), find_reply)
	#Ogni volta che ricevo una richiesta devo andare a prendere la risposta dal file di report corrispondente
	#Come argomento viene passata la cartella dei file di report per il test

	#Devi trovare un modo per ricevere id della richiesta e metterlo al nome del file
	#In questo modo vado ad aprire il file corrispondente e leggo la parte di reply

   # print("Mockup connesso. File passato: "+sys.argv[1])
	while True:
		print("---------------open server-------------------")
		#if server.got(OpMsg('find', 'test_collection', filter={})):
		#if server.got(OpMsg('find', 'test_collection')):
		#timeout in secondi
		#if server.receives(OpMsg('find', 'test_collection'),timeout=1000):
		if server.got(OpMsg('find', 'db', filter={"key":{"author":1,"changeId":1},"ns":"db.dbchangelog"}),timeout=1000):
			print("OP:Find")
			find_reply = OpReply({
			"cursor":{"firstBatch":[],"id":{"$numberLong":"0"},
				"ns":"db.system.indexes"},
			"ok":1.0
			})
			server.reply(find_reply)
		else:
			print("in attesa di comando")
			# try:
			#     server.receives(timeout=0.1)
			# except AssertionError as err:
			#     print("Error: %s" % err)
			cmd = server.receives(timeout=30)
			print(cmd)
			print(cmd.command_name)
			if str(cmd) == "{\"find\": \"system.indexes\", \"filter\": {\"ns\": \"db.dbchangelog\", \"key\": {\"changeId\": 1, \"author\": 1}}, \"limit\": 1, \"singleBatch\": true}":
				# find_reply = OpReply({
				#  	"cursor": {"firstBatch": [], "id": {"$numberLong": "0"},
				#  			   "ns": "db.system.indexes"}
				# })
				# cmd.ok(find_reply)
				find_reply = OpReply({
					"cursor":{
						"createdCollectionAutomatically":True,
						"numIndexesAfter":2,
						"numIndexesBefore":1,
						"id":Int64(0),
						"firstBatch": [],
						"ns": "db.system.indexes"
					},
					"ok":1.0
				})
				print("risposta con: "+str(find_reply))
				cmd.replies(find_reply)
				#cmd.ok(cursor={'firstBatch': [], 'id': {'$numberLong': 0},'ns': 'db.system.indexes'})
			else:
				general_reply = OpReply({
					"n":1,
					"ok": 1.0
				})
				#cmd.ok()
				cmd.replies(general_reply)
		#if server.got('shutdown'):
	server.stop()
	print("---------------close server---------------------")

if __name__ == "__main__":
	main()
