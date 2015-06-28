import os
import os.path
'''
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askdirectory() # show an "Open" dialog box and return the path to the selected file
print(filename)
'''


print "Grabbing Invisibility Cloak..."
folder = "/home/mithrandir/Test"
log = folder+"log.txt"
prefix = "data"
count = 0
f = open('log.txt','w')


print root


for dirpath, dirnames, filenames in os.walk(folder):
    for filename in filenames:
    	name = os.path.join(dirpath,filename)
    	new_name = os.path.join(dirpath,prefix+str(count))+".data"
    	count = count+1
        #print os.path.join(dirpath, filename)
        #print filename
        f.write(name+"\n"+new_name+"\n")
        os.rename(name,new_name)


print "Whooosh...\nHuh. Where did you go? :O"

f.close()

