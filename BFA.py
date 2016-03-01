__author__ = 'AravindMac'

import os
import copy
from math import sqrt
from math import exp

fingerprint = [0]*256
correlation_factor=[0]*256
pnf = 0
sigma = 0.0375

#inputDir = sys.argv[1]
inputDir = str(os.getcwd())
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

                    for i in range(len(normalized_freq_distribution)):
                        normalized_freq_distribution[i] = sqrt(normalized_freq_distribution[i]/(maxFreq*1.0))

                    for i in range(len(fingerprint)):
                        fingerprint[i] = ((fingerprint[i] * pnf) + normalized_freq_distribution[i])/(pnf + 1)

                    for i in range(len(correlation_factor)):
                        x=normalized_freq_distribution[i]-fingerprint[i]
                        correlation_factor[i]=exp(-(x*x)/(2*sigma*sigma))

                    pnf += 1

with open("BFA_fingerprint","wb") as f:
    f.write(str(fingerprint))
print fingerprint
