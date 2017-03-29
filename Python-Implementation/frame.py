import cv2
import numpy as np

class Frame(object):
	def __init__(self, path):
		self.path = path
		self.frame = cv2.imread(path, 0)
		self.frame = cv2.resize(self.frame, (0,0), fx=0.05, fy=0.05)
	
	def get_path(self):
		return self.path
	
	def get_frame(self):
		return self.frame
	
	def set_path(self, path):
		self.path = path
	
	def set_frame(self, frame):
		self.frame = frame
	
	def __str__(self):
		return self.path+'\n'+str(self.frame)