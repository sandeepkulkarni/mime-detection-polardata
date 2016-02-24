__author__ = 'AravindMac'

import os
import copy
from math import exp

pnf = 0
sigma = 0.0375
n = 256
matrix = [[0 for i in range(n)]for i in range(n)]
fingerprint = [[0 for i in range(n)]for i in range(n)]

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
                        normalized_freq_distribution[i] /= maxFreq*1.0

                    #print normalized_freq_distribution


                    for i in range(n):
                        for j in range(n):
                            if i<j:
                                matrix[i][j] = normalized_freq_distribution[j] - normalized_freq_distribution[i]
                                fingerprint[i][j]=((fingerprint[i][j]*pnf)+matrix[i][j])/(pnf+1)           #Upper Half of Matrix
                                #print("first : "+str(fingerprint[i][j]))
                                x=matrix[i][j]-fingerprint[i][j]
                                #if x>0:
                                    #print i,j
                                    #print "x: "+str(x)
                                correlation=exp(-(x*x)/(2*sigma*sigma))                                 #Lower Half of Matrix
                            #    if correlation>1:
                            #        print "C : "+str(correlation)
                                fingerprint[j][i] = ((fingerprint[j][i]*pnf)+correlation)/(pnf+1)
                                #print("second: "+str(fingerprint[j][i]))

                    fingerprint[0][0] = pnf

                    pnf+=1

with open("BFC_fingerprint","wb") as f:
    f.write(str(fingerprint))
print fingerprint
