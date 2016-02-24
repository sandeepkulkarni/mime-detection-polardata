__author__ = 'AravindMac'

import os

def move(src,dest,num):
    i=0
    for f in os.listdir(src):
        if not f.startswith("."):
            if(i<num):
                srcPath = src+"/"+f
                destPath = dest+"/"+f
                os.system ("mv"+ " " + srcPath + " " + destPath)
                i+=1
            else:
                break

if __name__ == '__main__':

    path = os.getcwd()+"/images"
    trainPath = os.getcwd()+"/train"
    testPath = os.getcwd()+"/test"
    numFiles = len([name for name in os.listdir(path) if not name.startswith(".")])

    numTrainFiles = int(0.75*numFiles)
    numTestFiles = numFiles - numTrainFiles

    print numFiles
    print numTrainFiles
    print numTestFiles


    move(path,trainPath,numTrainFiles)
    move(path,testPath,numTestFiles)