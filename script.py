__name__ = "vutsuak"

import os
import time


def file_size(l):
    return "SIZE IS: "+str(l[6] * .001) + " KB"


def modification_time(l):
    return time.ctime(l[7])


def metadata_change_time(l):
    return time.ctime(l[9])

def word_count(path):
    f=open(path)
    return len(f.read())


def filestat(path):
    l = list(os.stat(path))
    print file_size(l)
    print "LAST MODIFIED ON: " + str(modification_time(l))
    print "LAST CHANGE IN METADATA: " + str(metadata_change_time(l))
    print "THE WORD COUNT IS "+str(word_count(path))

if __name__ == "vutsuak":
    filestat("C:\Users\windows 7\Desktop\Reading Between The Lines.docx")
