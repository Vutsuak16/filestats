__name__ = "vutsuak"

import os
import time


def file_size(l):
    return str(l[6] * .001) + " KB"


def modification_time(l):
    return time.ctime(l[7])


def metadata_change_time(l):
    return time.ctime(l[9])


def filestat(path):
    l = list(os.stat(path))
    print file_size(l)
    print "last modified on " + str(modification_time(l))
    print "last change in metadata " + str(metadata_change_time(l))


if __name__ == "vutsuak":
    filestat("C:\Users\windows 7\Desktop\Reading Between The Lines.docx")
