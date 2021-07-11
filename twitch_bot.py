import pyautogui
from PIL import ImageGrab, ImageOps
import time
from numpy import *

box = (1611,981, 1652, 1011)
def imageGrab():
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a  = array(grayimage.getcolors())
    return a.sum()

while True:
    if imageGrab() != 1485:
        pyautogui.click(1630, 1000)
    
