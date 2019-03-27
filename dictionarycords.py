#Dictionary List for all the 

cords = {}

def dictionarycords():
    #tkinter input; title
    cords[1] = 20; cords[2] = 840
    cords[3] = 535; cords[4] = 920

    #name
    cords[5] = 20; cords[6] = 920
    cords[7] = 535; cords[8] = 1030

    #Lv.
    cords[9] = 145; cords[10] = 1100
    cords[11] = 435; cords[12] = 1170

    #Stat no.
    cords[13] = 80; cords[14] = 1190
    cords[15] = 490; cords[16] = 1260

    cords[18] = 1265
    cords["disty1"] = cords[18] - cords[16]
    cords["disty2"] = cords[16] - cords[14]

    for i in range(17, 36, 4):
        cords[i] = cords[13]; cords[i+2] = cords[15]
        cords[i+1] = cords["disty1"] + cords[i - 1]; cords[i+3] = cords["disty2"] + cords[i + 1]

    #Skills
    cords[37] = 625; cords[38] = cords[14]
    cords[39] = 1000; cords[40] = cords[16]

    for i in range(41, 60, 4):
        cords[i] = cords[37]; cords[i+2] = cords[39]
        cords[i+1] = cords["disty1"] + cords[i - 1]; cords[i+3] = cords["disty2"] + cords[i + 1]

dictionarycords()


