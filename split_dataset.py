import os
import shutil
import glob

def move(src,dest,num):
    i=0
    for f in os.listdir(src):
        if not f.startswith("."):
            if(i<num):
                srcPath = src+"/"+f
                destPath = dest+"/"+f
                shutil.move(srcPath, destPath)
                #os.system ("mv"+ " " + srcPath + " " + destPath)
                i+=1
            else:
                break

if __name__ == '__main__':

    path = os.path.normpath("F:/polardata_sorted/application_octet-stream")
    trainPath = os.path.normpath("F:/polardata_chosen/application_octet-stream_train")
    testPath = os.path.normpath("F:/polardata_chosen/application_octet-stream_test")

    for filename in glob.iglob(os.path.join(path, '*')):
        if os.stat(filename).st_size == 0:
            os.remove(filename)
            print filename

    numFiles = len([name for name in os.listdir(path) if not name.startswith(".")])

    numTrainFiles = int(0.75*numFiles)
    numTestFiles = numFiles - numTrainFiles

    print numFiles
    print numTrainFiles
    print numTestFiles

    move(path,trainPath,numTrainFiles)
    move(path,testPath,numTestFiles)