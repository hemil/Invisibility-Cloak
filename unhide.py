import os
import os.path

print "Pine Fresh."
print "Revert to Form.\nRemoving the cloak..."
oldname = 0
newname = 1

'''
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askdirectory() # show an "Open" dialog box and return the path to the selected file
print(filename)
'''

new = []
folder = "/home/mithrandir/Test"
log = folder+'log.txt'
lines = [line.rstrip('\n') for line in open('log.txt')]

#print lines

for i in xrange(len(lines)/2):
	TrueName = lines[oldname]
	FalseName = lines[newname]
	os.rename(FalseName,TrueName)
	#print lines[i]
	#print TrueName+" | "+FalseName
	oldname = oldname + 2
	newname = newname + 2

print "There and Back Again."