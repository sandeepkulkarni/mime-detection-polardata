import os
import shutil
import traceback
from tika import detector
import sys


rootdir=sys.argv[1] #input dir
outdir=sys.argv[2]   #output dir

#dirwalk
for root, subdirs, files in os.walk(rootdir):
    for file in files:
        try:
            if(os.path.isdir(os.path.join(root,file))):
                continue
            #detect the mime type using Tika
            detect=detector.from_file(os.path.join(root,file))
            result=detect.replace("/","_")


            #create a directory in the output folder with the mime type name
            dirname=os.path.join(outdir,result)

            if not os.path.exists(dirname):
                os.makedirs(dirname)

            #move the file to the directory
            shutil.move(os.path.join(root,file), os.path.join(dirname,file))
            if not (os.path.exists(os.path.join(dirname,file))):
                print("Something went wrong!")

        except OSError as exc:
            print(exc.strerror)

        except Exception, err:
            print(traceback.format_exc())
            continue