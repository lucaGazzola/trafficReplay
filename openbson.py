import bson
import sys
bson_file = sys.argv[1]
with open(bson_file,'rb') as f:
    data = bson.decode_all(f.read())
print(data)