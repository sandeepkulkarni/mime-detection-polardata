__author__ = 'AravindMac'


import os
import sys

headerSize = 28
header_bytes = [4,8,16]
offset = 4
n=256
pnf=0
old_fingerprint = [[0 for i in range(n)]for i in range(headerSize)]
current_fingerprint = [[0 for i in range(n)]for i in range(headerSize)]

#inputDir = sys.argv[1]
inputDir = str(os.getcwd())
for root, dirnames, files in os.walk(inputDir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in files:
            if not filename.startswith('.'):
                with open(os.path.join(root, filename),"rb") as File:
                    f = File.read()
                    b = bytearray(f)
                    ind = 0
                    start = 0
                    end = header_bytes[0]
                    header_array = []
                    while(ind < len(header_bytes)):
                        for i in range(start,end):
                            header_array.append(b[i])
                        start = end + offset
                        ind+=1
                        if(ind <= len(header_bytes)-1):
                            end = start + header_bytes[ind]
                    print filename, header_array

                    if(len(header_array) > len(b)):
                        continue

                    for i in range(len(header_array)):
                        old_fingerprint[i][header_array[i]]=1
                    for i in range(headerSize):
                        for j in range(n):
                            if(current_fingerprint[i][j] == 0 and old_fingerprint[i][j] == 0):
                                continue
                            else:
                                current_fingerprint[i][j]=((current_fingerprint[i][j]*pnf)+old_fingerprint[i][j])/(pnf+1)*1.0
                    pnf+=1

print current_fingerprint
