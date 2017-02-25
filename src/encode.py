import sys
import os
import time 


print("Please ensure that your .txt  file is in the same path directory.")

filename = raw_input('Enter file name: ')

checklast = list(filename)

if (checklast[len(checklast)-1]=="8"):
	print ("This file has already been encoded.")
	exit()
	
newfilename = filename[:-1]
newfilename += str("8.txt")
filename += str(".txt")

print ("Encoding " + filename + " . Please wait")


#Time Recording Start
millis1 = int(round(time.time() * 1000))


file = open(filename,"r+")
text = list(file.read())
file.close()

file = open(filename, "w+")
st = ""
for letter in text:
	if (letter == 'a'):
		st+=str('1')
	if (letter == 'b'):
		st+=str('2')
	if (letter == 'c'):
		st+=str('3')
	if (letter == 'd'):
		st+=str('4')
	if (letter == 'e'):
		st+=str('5')
	if (letter == 'f'):
		st+=str('6')		
	if (letter == 'g'):
		st+=str('7')
	if (letter == 'h'):
		st+=str('8')
	if (letter == 'i'):
		st+=str('9')
	if (letter == 'j'):
		st+=str('a')
	if (letter == 'k'):
		st+=str('b')
	if (letter == 'l'):
		st+=str('c')
	if (letter == 'm'):
		st+=str('d')
	if (letter == 'n'):
		st+=str('e')
	if (letter == 'o'):
		st+=str('f')
	if (letter == 'p'):
		st+=str('g')
	if (letter == 'q'):
		st+=str('h')
	if (letter == 'r'):
		st+=str('i')
	if (letter == 's'):
		st+=str('j')
	if (letter == 't'):
		st+=str('k')
	if (letter == 'u'):
		st+=str('l')
	if (letter == 'v'):
		st+=str('m')
	if (letter == 'w'):
		st+=str('n')
	if (letter == 'y'):
		st+=str('o')
	if (letter == 'z'):
		st+=str('p')		
	if (letter == ' '):
		st+=str(' ')

file.write(st)


#Time Recording Start
millis2 = int (round(time.time() * 1000))

#Printing the performance gauge timing 
print ("\n")
print ("Time taken for encoding process:") ,((millis2 - millis1) * 1000) ,("microseconds.")
print ("\n")


file.close()
print("\n")
print(filename + " is now " + newfilename)
print("\n")
os.rename(filename,newfilename)