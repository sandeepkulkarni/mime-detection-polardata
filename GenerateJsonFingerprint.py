import os
import json

fpFile = "BFA_fingerprint"
inputFile = str(os.getcwd()) + "\\" + fpFile

file = open(inputFile,"r")

fingerprint = file.readline()

str = fingerprint[1:-1]
arr = str.split(",")

print arr

records = []
for id, val in enumerate(arr):
    print id
    print float(val)
    record = {'index_gzip':id, 'frequency':val}
    records.append(record)

json_data = json.dumps({'gzip': records})
print json_data