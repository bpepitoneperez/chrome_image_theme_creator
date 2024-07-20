# Importing Image class from PIL module 
from PIL import Image, ImageEnhance
import zipfile
import os
 
# Opens a image in RGB mode 
original = Image.open(r"original.jpg")

bg = original.resize((2560, 1440))
bg.save("bg.png")
 
# Size of the image in pixels (size of original image) 
# (This is not mandatory) 
width, height = bg.size 
 
# Setting the points for frame 
frameLeft = 0
frameTop = 0
frameRight = width
frameBottom = 45
 
# Cropped image of above dimension
frameImage = bg.crop((frameLeft, frameTop, frameRight, frameBottom))
frameImage.save("frame.png")


# Setting the points for toolbar 
toolbarLeft = 0
toolbarTop = frameBottom
toolbarRight = width
toolbarBottom = frameBottom + 120
 
# Cropped image of above dimension
toolbarImage = bg.crop((toolbarLeft, toolbarTop, toolbarRight, toolbarBottom))
toolbarImage.save("toolbar.png")


# Setting the points for toolbarBG 
tabBGLeft = 0
tabBGTop = 0
tabBGRight = width
tabBGBottom = 45
 
# Cropped image of above dimension
tabBGImage = bg.crop((tabBGLeft, tabBGTop, tabBGRight, tabBGBottom))
enhancer = ImageEnhance.Brightness(tabBGImage)
# to reduce brightness by 20%, use factor 0.8
tabBGImage = enhancer.enhance(0.8)
tabBGImage.save("tab_background.png")

# Create ZIP
zf = zipfile.ZipFile("theme.zip", "w")
zf.write("./manifest.json")
zf.write("./bg.png")
zf.write("./frame.png")
zf.write("./toolbar.png")
zf.write("./tab_background.png")
zf.close()

os.remove("./bg.png")
os.remove("./frame.png")
os.remove("./toolbar.png")
os.remove("./tab_background.png")