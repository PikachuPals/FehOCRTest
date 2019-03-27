from PIL import Image
from pytesseract import *
from dictionarycords import *
from imagemanip import *
import re

global temp
temp = 0

def listOut(file):
    valueList = []
    global temp
    image = Imagemanip(file)
    output = values(image, 1, valueList)
    temp += 1
    output.insert(0, temp)
    output.append(0)
    return output

def OCR(image_file):
    pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    im = Image.open(image_file)
    tessdata_dir_config = '--tessdata-dir"C:\Program Files (x86)\Tesseract-OCR\tessdata"'
    text = image_to_string(im, lang = 'eng', config=tessdata_dir_config)
    return text

def values(image, count, valueList):
    numbers = re.compile('\d+')
    
    if count < 60:
        crop = image.crop((cords[count], cords[count+1], cords[count+2], cords[count+3]))
        crop.save('test2.png')
        count +=4

        if count < 14 or count > 37:    
            text = OCR("test2.png")
            valueList.append(text)
        else:
            text = OCR("test2.png")
            text = numbers.search(text).group(0)
            valueList.append(text)

        values(image, count, valueList)
    
    else:
        return valueList
    return valueList  
