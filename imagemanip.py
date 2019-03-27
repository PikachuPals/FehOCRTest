from PIL import Image

def Imagemanip(file):
    #Convert RGBA to RGB - (Only run once per image)

    image = Image.open(file)
    if image.mode == "RGBA":
        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])
        background.save(file)
    else:
        pass

    #Loads image into ram  - creates new list for image pixel colours

    image = Image.open(file)
    pxls = image.getdata()
    npxls = []

    #Replacing colours to allow tesseract to work easier + making text clearer

    for r, g, b in pxls:
        #change background to green
        if (r, g, b) != (10, 30, 50) and (r,g,b) != (9, 36, 50) and (r, g, b) != (50, 30, 10) and (r, g, b) != (255, 255, 255) and (r, g, b) != (254, 249, 149) and (r, g, b) != (254, 254, 254) and (r, g, b) != (130, 245, 70):
            change = (50, 93, 101)
            npxls.append(change)
        #change text border to background
        elif (r, g, b) == (10, 30, 50) or (r, g, b) == (9, 36, 50) or (r, g, b) == (50, 30, 10) and (r, g, b) != (254, 249, 149):
            change = (50, 93, 101)
            npxls.append(change)
        #change text colours to black
        else:
            npxls.append((0,0,0))

    #New image creation

    newimage = Image.new(image.mode, image.size)
    newimage.putdata(npxls)
    #newimage.save('screenshot2.png')
    return newimage
