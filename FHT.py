__author__ = 'AravindMac'

import os
import sys
import json

inputDir = sys.argv[1]         #Path to the input directory
headerSize = int(sys.argv[2])         #Specify the header size


n=256
pnf=0
old_fingerprint = [[0 for i in range(n)]for i in range(headerSize)]
current_fingerprint = [[0 for i in range(n)]for i in range(headerSize)]
counter=0

#Dirwalk
for root, dirnames, files in os.walk(inputDir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in files:
            if not filename.startswith('.'):
                with open(os.path.join(root, filename),"rb") as File:
                        #read file as bytearray
                        f = File.read()
                        b = bytearray(f)

                        #if length of the file is less than headersize, skip the file
                        if len(b) < headerSize:
                                continue
                        else:
                                header_array = []
                                for i in range(headerSize) :
                                        header_array.append(b[i])

                        #compute the fingerprint
                        for i in range(len(header_array)):
                                old_fingerprint[i][header_array[i]]=1
                        for i in range(headerSize):
                                for j in range(n):
                                        if(current_fingerprint[i][j] == 0 and old_fingerprint[i][j] == 0):
                                                continue
                                        else:
                                                current_fingerprint[i][j]=((current_fingerprint[i][j]*pnf)+old_fingerprint[i][j])/(pnf+1)*1.0
                        pnf+=1


#print fingerprint to json
with open("FHT_fingerprint.json","ab") as f:
    data = []
    for i in range(headerSize):
        for j in range(n):
            link = {'source':i, 'target':j, 'frequency':abs(current_fingerprint[i][j])}
            data.append(link)

    json_data = json.dumps(data)

    f.write(json_data)
counter+=1
