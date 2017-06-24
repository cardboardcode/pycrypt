import sys
import os

def encryptFile(st, text):
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
		if (letter == 'x'):
			st+=str('o')	
		if (letter == 'y'):
			st+=str('p')
		if (letter == 'z'):
			st+=str('q')		
		if (letter == ' '):
			st+=str(' ')
		#Capital Letters Lexicon start
		if (letter == 'A'):
			st+=str('Z')
		if (letter == 'B'):
			st+=str('Y')
		if (letter == 'C'):
			st+=str('X')
		if (letter == 'D'):
			st+=str('W')
		if (letter == 'E'):
			st+=str('V')
		if (letter == 'F'):
			st+=str('U')
		if (letter == 'G'):
			st+=str('T')
		if (letter == 'H'):
			st+=str('S')
		if (letter == 'I'):
			st+=str('R')
		if (letter == 'J'):
			st+=str('Q')
		if (letter == 'K'):
			st+=str('P')
		if (letter == 'L'):
			st+=str('O')
		if (letter == 'M'):
			st+=str('N')
		if (letter == 'N'):
			st+=str('M')
		if (letter == 'O'):
			st+=str('L')
		if (letter == 'P'):
			st+=str('K')
		if (letter == 'Q'):
			st+=str('J')
		if (letter == 'R'):
			st+=str('I')
		if (letter == 'S'):
			st+=str('H')
		if (letter == 'T'):
			st+=str('G')
		if (letter == 'U'):
			st+=str('F')
		if (letter == 'V'):
			st+=str('E')
		if (letter == 'W'):
			st+=str('D')
		if (letter == 'X'):
			st+=str('C')
		if (letter == 'Y'):
			st+=str('B')
		if (letter == 'Z'):
			st+=str('A')	
	
	return st

def decryptFile(st, text):
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
		#Capital Letters Lexicon start
		if (letter == 'A'):
			st+=str('Z')
		if (letter == 'B'):
			st+=str('Y')
		if (letter == 'C'):
			st+=str('X')
		if (letter == 'D'):
			st+=str('W')
		if (letter == 'E'):
			st+=str('V')
		if (letter == 'F'):
			st+=str('U')
		if (letter == 'G'):
			st+=str('T')
		if (letter == 'H'):
			st+=str('S')
		if (letter == 'I'):
			st+=str('R')
		if (letter == 'J'):
			st+=str('Q')
		if (letter == 'K'):
			st+=str('P')
		if (letter == 'L'):
			st+=str('O')
		if (letter == 'M'):
			st+=str('N')
		if (letter == 'N'):
			st+=str('M')
		if (letter == 'O'):
			st+=str('L')
		if (letter == 'P'):
			st+=str('K')
		if (letter == 'Q'):
			st+=str('J')
		if (letter == 'R'):
			st+=str('I')
		if (letter == 'S'):
			st+=str('H')
		if (letter == 'T'):
			st+=str('G')
		if (letter == 'U'):
			st+=str('F')
		if (letter == 'V'):
			st+=str('E')
		if (letter == 'W'):
			st+=str('D')
		if (letter == 'X'):
			st+=str('C')
		if (letter == 'Y'):
			st+=str('B')
		if (letter == 'Z'):
			st+=str('A')

	return st