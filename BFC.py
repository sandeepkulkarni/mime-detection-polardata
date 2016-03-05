__author__ = 'AravindMac'

import os
import copy
from math import sqrt
from math import exp
import json
import sys

pnf = 0
sigma = 0.0375
n = 256
matrix = [[0 for i in range(n)]for i in range(n)]
fingerprint = [[0 for i in range(n)]for i in range(n)]

inputDir = sys.argv[1] #path to input directory

#directory walk
for root, dirnames, files in os.walk(inputDir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in files:
            if not filename.startswith('.'):
                with open(os.path.join(root, filename),"rb") as File:
                    #read the file as a byte array

                    f = File.read()
                    b = bytearray(f)


                    #compute the frequency distribution
                    freq_distribution=[0]*256

                    for i in range(len(b)):
                        freq_distribution[b[i]] += 1

                    maxFreq = max(freq_distribution)
                    normalized_freq_distribution = copy.deepcopy(freq_distribution)

                    #normalize
                    if (maxFreq):
                        for i in range(len(normalized_freq_distribution)):
                            normalized_freq_distribution[i] = sqrt(normalized_freq_distribution[i]/(maxFreq*1.0))
                    else:
                        continue

                    #compute the fingerprint
                    for i in range(n):
                        for j in range(n):
                            if i<j:
                                matrix[i][j] = normalized_freq_distribution[j] - normalized_freq_distribution[i]
                                fingerprint[i][j]=((fingerprint[i][j]*pnf)+matrix[i][j])/(pnf+1)           #Upper Half of Matrix
                                x=matrix[i][j]-fingerprint[i][j]
                                correlation=exp(-(x*x)/(2*sigma*sigma))                                 #Lower Half of Matrix
                                fingerprint[j][i] = ((fingerprint[j][i]*pnf)+correlation)/(pnf+1)

                    fingerprint[0][0] = pnf

                    pnf+=1

#write to JSON File
with open("BFC_fingerprint.json","wb") as f:
    data = []
    for i in range(0,n,5):
        data.append(str(i))
    json_data = json.dumps(data)


    data = []
    for i in range(n):
        for j in range(n):
            link = {'source':i, 'target':j, 'frequency':abs(fingerprint[i][j])}
            data.append(link)

    json_data = json.dumps(data)

    f.write(json_data)

