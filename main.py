import pyautogui
from PIL import Image
import pytesseract

from pymouse import PyMouseEvent

xy1 = xy2 = None

class ListenInterrupt(Exception):
	pass

class Clickonacci(PyMouseEvent):

	def click(self, x, y, button, press):
		global xy1, xy2
		'''Print Fibonacci numbers when the left click is pressed.'''
		print(button, press, xy1, xy2)
		if button == 1:
			if press:
				xy1 = x,y
			else:
				xy2 = x,y
				raise ListenInterrupt("Finished")

print("Select the region now")
C = Clickonacci()
try:
	C.run()
except ListenInterrupt:
	pass

def get_text(image):
	return pytesseract.image_to_string(image, config='-psm 6')

xy_min = (min(xy2[0],xy1[0]), min(xy2[1],xy1[1]))
xy_max = (max(xy2[0],xy1[0]), max(xy2[1],xy1[1]))
wh = (xy_max[0]-xy_min[0], xy_max[1]-xy_min[1])

pyautogui.screenshot('screen.png',region=(*xy_min, *wh))
img = Image.open('screen.png')
text = get_text(img)
print(text)
