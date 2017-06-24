import sys
import os


def isEncrypted(checklast):

	return checklast[len(checklast)-1]=="8"
	
def isDecrypted(checklast):
	return checklast[len(checklast)-1]=="0"
