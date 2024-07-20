from PIL import Image, ImageEnhance
import zipfile
import os
 
# Opens original image
original = Image.open(r"original.jpg")

width = 2560
height = 1440

#Resize to seleceted resolution
bg = original.resize((width, height))
bg.save("bg.png")
 
# Create frame
frameLeft = 0
frameTop = 0
frameRight = width
frameBottom = 45

frameImage = bg.crop((frameLeft, frameTop, frameRight, frameBottom))
frameImage.save("frame.png")


# Create toolbar
toolbarLeft = 0
toolbarTop = frameBottom
toolbarRight = width
toolbarBottom = frameBottom + 120

toolbarImage = bg.crop((toolbarLeft, toolbarTop, toolbarRight, toolbarBottom))
toolbarImage.save("toolbar.png")

# Create toolbarBG 
tabBGLeft = 0
tabBGTop = 0
tabBGRight = width
tabBGBottom = 45

tabBGImage = bg.crop((tabBGLeft, tabBGTop, tabBGRight, tabBGBottom))
enhancer = ImageEnhance.Brightness(tabBGImage)
# Reduce brightness
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

# Remove created images
os.remove("./bg.png")
os.remove("./frame.png")
os.remove("./toolbar.png")
os.remove("./tab_background.png")