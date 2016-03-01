__author__ = 'AravindMac'

import os
import sys
import copy
from math import sqrt
from math import exp
import json

fingerprint = [0]*256
correlation_factor=[0]*256
pnf = 0
sigma = 0.0375

# Reading from command line arguments

#inputDir = sys.argv[1]         #Path to the input directory
#mimetype = sys.argv[2]         #Specify mimetype

# Reading from default values

inputDir = str(os.getcwd())
mimetype = "jpeg"

#bf = open("BFA_NN_datasetR","ab")

for root, dirnames, files in os.walk(inputDir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in files:
            if not filename.startswith('.'):
                with open(os.path.join(root, filename),"rb") as File:
                    f = File.read()
                    b = bytearray(f)
                    #for i in range(len(b)):
                    #    print b[i]
                    freq_distribution=[0]*256

                    for i in range(len(b)):
                        freq_distribution[b[i]] += 1

                    maxFreq = max(freq_distribution)
                    normalized_freq_distribution = copy.deepcopy(freq_distribution)

                    if(maxFreq):
                        for i in range(len(normalized_freq_distribution)):
                            normalized_freq_distribution[i] = sqrt(normalized_freq_distribution[i]/(maxFreq*1.0))
                    else:
                        continue

                    """
                    bf.write(str(maxFreq)+"\t")
                    for i in normalized_freq_distribution:
                        bf.write(str(i)+"\t")
                    bf.write(str(0))
                    bf.write("\n")
                    """
                    for i in range(len(fingerprint)):
                        fingerprint[i] = ((fingerprint[i] * pnf) + normalized_freq_distribution[i])/(pnf + 1)

                    """
                    for i in range(len(correlation_factor)):
                        x=normalized_freq_distribution[i]-fingerprint[i]
                        correlation_factor[i]=exp(-(x*x)/(2*sigma*sigma))
                    """
                    pnf += 1


#Generating training and testing dataset for modelfile.

"""
bf.close()

bf2 = open("BFA_NN_datasetR","rb")
train = open("train.csv","ab")
test = open("test.csv","ab")

bf2.seek(0,0)
numLines = 0
for line in bf2.readlines():
    numLines+=1

bf2.seek(0,0)

trainLength = int(numLines*0.75)
count=0
for line in bf2.readlines():
    if(count <= trainLength):
        train.write(line)
    else:
        test.write(line)
    count+=1
"""

#Writing fingerprint to file

with open("BFA_fingerprint","wb") as f:
    f.write(str(fingerprint))
f.close()
print fingerprint

#Generating fingerprint in JSON format

records = []
for id, val in enumerate(fingerprint):
    record = {'index':id, 'mimetype':mimetype, 'frequency':val}
    records.append(record)
print json.dumps(records, sort_keys=True, indent=4, separators=(',', ': '))

#Writing JSON to file

with open("BFA_JSON_OUTPUT","wb") as f:
    f.write(json.dumps(records, sort_keys=True, indent=4, separators=(',', ': ')))
f.close()
