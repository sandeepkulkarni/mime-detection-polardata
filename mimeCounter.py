import os
import tika
from tika import detector
import traceback
import json

#specify a list of directories as input
rootdirs=[os.path.normpath("E:/polardata_chosen/"),
          os.path.normpath("E:/polardata_octet/"),
          os.path.normpath("E:/polardata_sorted/")]

mimetypes={}
for rootdir in rootdirs:
    #dirwalk
    for root, subdirs, files in os.walk(rootdir):
        for file in files:
            try:

                if(os.path.isdir(os.path.join(root,file))):
                    continue
                #use tika to detect the mime type
                detect=detector.from_file(os.path.join(root,file))

                #build the dictionary of the mime-type and count of files of that mime type
                if detect in mimetypes:
                    mimetypes[detect]+=1
                else:
                    mimetypes[detect]=1
            except OSError as exc:
                print(exc.strerror)
                continue
            except Exception, err:
                print(traceback.format_exc())
                continue


#print the mime type counts to a json file
with open('data.json', 'w') as fp:
    json.dump(mimetypes, fp)
