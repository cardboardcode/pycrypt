import sys
import os

filename = "report.txt"
encodeTime = 0
decodeTime = 0

isEncode = 1

with open(filename, "r+") as f:
	for line in f:
		if (isEncode == 1):
			tempTime1 = line.rstrip
			tempTime1 = int(line)
			encodeTime = encodeTime + tempTime1
			isEncode = 0
		elif(isEncode == 0):
			tempTime2 = line.rstrip
			tempTime2 = int(line)
			decodeTime = decodeTime + tempTime2
			isEncode = 1

			
averageEncode = "Average time taken for encoding: " + str(encodeTime/5) + " microseconds"
averageDecode = "Average time taken for decoding: " + str(decodeTime/5) + " microseconds"

file = open(filename, "w+")

foo = averageEncode + "\n" + averageDecode
file.write(foo)

file.close()