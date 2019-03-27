from PIL import Image, ImageDraw
from dictionarycords import *

image = Image.open("screenshot.png")
d = ImageDraw.Draw(image)

def values(image, count,d):
    
    if count < 60:
        d.rectangle((cords[count], cords[count+1], cords[count+2], cords[count+3]),outline = "Black")
        count +=4

        values(image, count, d)
    
    else:
        return d
    return d

values(image,1,d)
image.show()
