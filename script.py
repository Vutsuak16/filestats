__name__ = "vutsuak"

import os
import time
from docx import Document
import re


def file_size(l):
    return str(l[6] * .001)


def modification_time(l):
    return time.ctime(l[7])


def metadata_change_time(l):
    return time.ctime(l[9])


def word_count(path):
    space = re.compile("\s+")
    line = re.compile("\\n+")
    ext = path.split(".")[1]
    if ext == "docx":
        document = Document(path)
        docText = '\n\n'.join([paragraph.text.encode('utf-8') for paragraph in document.paragraphs])
        ct = 0
        word = ""
        for i in docText:
            if line.match(i):
                continue
            if space.match(i):  # two different matching techniques
                ct += 1
                word = ""
                continue
            word += i
        return ct

    elif ext == "txt":
        f = open(path)
        string = re.split(space, f.read())
        return len(string)


def filestat(path):
    l = list(os.stat(path))
    print "SIZE IS: " + file_size(l) + " KB"
    print "LAST MODIFIED ON: " + str(modification_time(l))
    print "LAST CHANGE IN METADATA: " + str(metadata_change_time(l))
    print "THE WORD COUNT IS " + str(word_count(path))


if __name__ == "vutsuak":
    filestat("C:\Users\windows 7\Desktop\jgjg.txt")
