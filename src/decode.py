import sys
import os
from statecheck import *
from timer import *
from parserlib import *

debugger = Timer()

#print("Please ensure that your .txt  file is in the same path directory.")
#filename = raw_input('Enter file name: ')
filename = input('')

checklast = list(filename)

if (isDecrypted(checklast)):
	print ("This file has already been decoded.")
	exit()

newfilename = filename[:-1]
newfilename += str("0.txt")
filename += str(".txt")

#print ("Decoding " + filename + ". Please wait")


#Time Recording Start
debugger.time_start()


file = open(filename,"r+")
text = list(file.read())
file.close()
file = open(filename, "w+") #Opening again in the write mode

st = ""
st = decryptFile(st, text)		
file.write(st)

#Time Recording Start
debugger.time_end()

#Printing the performance gauge timing 
#debugger.printUI()
debugger.printDebug()

file.close()
#print(filename + " is now " + newfilename)
os.rename(filename,newfilename)