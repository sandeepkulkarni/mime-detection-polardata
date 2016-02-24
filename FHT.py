__author__ = 'AravindMac'

import os
import sys

headerSize = 8
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
                        try:
                            f = File.read()
                            b = bytearray(f)
        
                            if len(b) < headerSize:
                                continue
                            else:
                                header_array = []
                                for i in range(headerSize) :
                                    header_array.append(b[i])
                            print filename, header_array
        
        
                            for i in range(len(header_array)):
                                old_fingerprint[i][header_array[i]]=1
                            for i in range(headerSize):
                                for j in range(n):
                                    if(current_fingerprint[i][j] == 0 and old_fingerprint[i][j] == 0):
                                        continue
                                    else:
                                        current_fingerprint[i][j]=((current_fingerprint[i][j]*pnf)+old_fingerprint[i][j])/(pnf+1)*1.0
                            pnf+=1
                        except OSError as exc:
                                print(exc.strerror)

                        except Exception, err:
                                print(traceback.format_exc())
                                continue
                                

with open("FHT_fingerprint","ab") as f:
    f.write(str(headerSize)+" "+str(current_fingerprint)+"\n")
print str(headerSize)+" "+str(current_fingerprint)
