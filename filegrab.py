import os
import re
from database import *
print(os.listdir("screenshots"))
png = re.compile('\.png')

images = os.listdir("screenshots")

for file in images:
    if png.search(file) !=  None:
        file = os.path.join(os.getcwd(),'screenshots',file)
        insertlist(listOut(file))
    else:
        pass

