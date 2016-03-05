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

inputDir = sys.argv[1]         #Path to the input directory
mimetype = sys.argv[2]         #Specify mimetype

#Directory walk
for root, dirnames, files in os.walk(inputDir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in files:
            if not filename.startswith('.'):
                with open(os.path.join(root, filename),"rb") as File:
                    #read the file as a byte array
                    f = File.read()
                    b = bytearray(f)
                    freq_distribution=[0]*256

                    #compute frequency distribution
                    for i in range(len(b)):
                        freq_distribution[b[i]] += 1

                    #normalize frequency distribution using max frequency
                    maxFreq = max(freq_distribution)
                    normalized_freq_distribution = copy.deepcopy(freq_distribution)

                    #use sqrt function as the companding function
                    if(maxFreq):
                        for i in range(len(normalized_freq_distribution)):
                            normalized_freq_distribution[i] = sqrt(normalized_freq_distribution[i]/(maxFreq*1.0))
                    else:
                        continue

                    #compute fingerprint
                    for i in range(len(fingerprint)):
                        fingerprint[i] = ((fingerprint[i] * pnf) + normalized_freq_distribution[i])/(pnf + 1)

                    #Compute the correlation factor
                    for i in range(len(correlation_factor)):
                        x=normalized_freq_distribution[i]-fingerprint[i]
                        correlation_factor[i]=exp(-(x*x)/(2*sigma*sigma))
                    pnf += 1


#Generating fingerprint in JSON format
records = []
for id, val in enumerate(fingerprint):
    record = {'index':id, 'mimetype':mimetype, 'frequency':str(val)}
    records.append(record)

#Writing JSON to file
with open("BFA_JSON_OUTPUT.json","wb") as f:
    f.write(json.dumps(records, sort_keys=True, indent=4, separators=(',', ': ')))
f.close()
