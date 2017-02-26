import sys
import os
from statecheck import *
from timer import * 
from parserlib import *

debugger = Timer();

try:
	input = raw_input
except NameError:
	pass

#UI
#print("Please ensure that your .txt  file is in the same path directory.")
#filename = raw_input('Enter file name: ')
filename = input('')

checklast = list(filename)

#Checking if whether the file is already encoded or not.
#If encoded, exit the program.
#Otherwise, resume encoding.
if (isEncrypted(checklast)):
	#print ("This file has already been encoded.")
	exit()

#Tweaking the filename to indicate proper state of encrypted file.	
#Remove the number at the end of the original filename. 	
newfilename = filename[:-1]
newfilename += str("8.txt")
filename += str(".txt")

#UI
#print ("Encoding " + filename + " . Please wait")


#Time Recording Start
debugger.time_start()


file = open(filename,"r+")
text = list(file.read())
file.close()
file = open(filename, "w+") #Opening again in the write mode

st = ""
st = encryptFile(st, text)	
file.write(st)

#Time Recording Start
debugger.time_end()

#Printing the performance gauge timing 
#debugger.printUI()
debugger.printDebug()


file.close()
#UI
#print(filename + " is now " + newfilename)
#Renaming done here
os.rename(filename,newfilename)

#End