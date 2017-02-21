import sys
import os

print("Please ensure that your .txt  file is in the same path directory.")

filename = raw_input('Enter file name: ')

checklast = list(filename)

if (checklast[len(checklast)-1]=="0"):
	print ("This file has already been decoded.")
	exit()

newfilename = filename[:-1]
newfilename += str("0.txt")
filename += str(".txt")

print ("Decoding " + filename + ". Please wait")

file = open(filename,"r+")
text = list(file.read())
file.close()

file = open(filename, "w+")
st = ""

for letter in text:
	if (letter == '1'):
		st+=str('a')
	if (letter == '2'):
		st+=str('b')
	if (letter == '3'):
		st+=str('c')
	if (letter == '4'):
		st+=str('d')
	if (letter == '5'):
		st+=str('e')
	if (letter == '6'):
		st+=str('f')		
	if (letter == '7'):
		st+=str('g')
	if (letter == '8'):
		st+=str('h')
	if (letter == '9'):
		st+=str('i')
	if (letter == 'a'):
		st+=str('j')
	if (letter == 'b'):
		st+=str('k')
	if (letter == 'c'):
		st+=str('l')
	if (letter == 'd'):
		st+=str('m')
	if (letter == 'e'):
		st+=str('n')
	if (letter == 'f'):
		st+=str('o')
	if (letter == 'g'):
		st+=str('p')
	if (letter == 'h'):
		st+=str('q')
	if (letter == 'i'):
		st+=str('r')
	if (letter == 'j'):
		st+=str('s')
	if (letter == 'k'):
		st+=str('t')
	if (letter == 'l'):
		st+=str('u')
	if (letter == 'm'):
		st+=str('v')
	if (letter == 'n'):
		st+=str('w')
	if (letter == 'o'):
		st+=str('y')
	if (letter == 'p'):
		st+=str('z')		
	if (letter == ' '):
		st+=str(' ')

file.write(st)

file.close()
print("\n")
print(filename + " is now " + newfilename)
print("\n")
os.rename(filename,newfilename)