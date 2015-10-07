import pytesseract
import os
from pytesseract import image_to_string
from PIL import Image

class ImageOcr(object):
	
	def __init__(self, filepath):
		if(os.path.isdir(filepath)):
			print "This is a directory and it can not be processed, please insert a picture!"
			return
		else:
			image = None
			try:
				image = Image.open(filepath)
			except Exception as exc:
				print str(exc)
				return
			
			if image is not None:
				self.image = image

	def to_string(self):
		return image_to_string(self.image)