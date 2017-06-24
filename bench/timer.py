import sys
import os
import time

class Timer:
	
	millis_start = 0
	millis_end = 0
	
	def __init__(self):   
		pass
	
	def getMillisStart(self):
		return self.millis_start
	
	def getMillisEnd(self):
		return self.millis_end	
	
	def time_start(self):
		self.millis_start = int(round(time.time()*1000))
	
	def time_end(self):
		self.millis_end = int(round(time.time()*1000))
		
	def printUI(self):
		print ("Time taken for encoding process:") ,((self.millis_end - self.millis_start) * 1000) ,("microseconds.")
		
	def printDebug(self):
		print(( self.millis_end - self.millis_start ) * 1000)