import os
import time

f=open("C:\Users\windows 7\Desktop\Reading Between The Lines.docx")

#print (os.stat("C:\Users\windows 7\Desktop\Reading Between The Lines.docx"))
x= list(os.stat("C:\Users\windows 7\Desktop\Reading Between The Lines.docx"))
print x[6]*.001
print time.localtime(x[7])
print time.localtime(x[8])