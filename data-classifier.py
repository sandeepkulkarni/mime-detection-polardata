import os
import shutil
import tika
from tika import parser
import traceback


#rootdir="/Users/rrgirish/Downloads"
rootdir=os.path.normpath("F:/datasetfull")
outdir=os.path.normpath("F:/polardata_sorted")



for root, subdirs, files in os.walk(rootdir):
    for file in files:
        try:
            if(os.path.isdir(os.path.join(root,file))):
                continue
            #send to tika server
            #result=os.popen("curl -X PUT --upload-file "+os.path.join(root, file)+" http://localhost:9988/detect/stream").read()
            parsed = parser.from_file(os.path.join(root, file))
            print file
            if("metadata" in parsed):
                if(type(parsed["metadata"]["Content-Type"])is list):
                    meta=parsed["metadata"]["Content-Type"][0]
                else:
                    meta=parsed["metadata"]["Content-Type"]
                meta=meta.split(";")[0]
            else:
                meta="application_octet-stream"
            result=meta.replace("/","_")
            dirname=os.path.join(outdir,result)


            if not os.path.exists(dirname):
                os.makedirs(dirname)
            shutil.move(os.path.join(root,file), os.path.join(dirname,file))
            if not (os.path.exists(os.path.join(dirname,file))):
                print("Something screwed up")

        except OSError as exc:
            print(exc.strerror)

        except Exception, err:
            print(traceback.format_exc())
            continue
