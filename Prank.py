import os
os.system("pip3 install Pillow pyscreenshot")
import pyscreenshot as ImageGrab
os.system("rm .screenshotprank.png")
im = ImageGrab.grab()
im.show()

im = ImageGrab.grab(bbox=(10, 10, 500, 500))
im.show()

ImageGrab.grab_to_file('.screenshotprank.png')
os.system("eog --fullscreen .screenshotprank.png")
