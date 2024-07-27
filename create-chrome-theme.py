from PIL import Image, ImageEnhance
import zipfile
import os
import argparse
import json

defaultWidth = 1920
defaultHeight = 1080
defaultTitle = "Created Chrome Theme"

parser = argparse.ArgumentParser(description='Creates a chrome theme given an image')
parser.add_argument('--res')
parser.add_argument('--title')

args = parser.parse_args()

if args.res is not None:
   if args.res == '1080p':
      width = 1920
      height = 1080
   elif args.res == '1440p':
      width = 2560
      height = 1440
   else:
      width = defaultWidth
      height = defaultHeight  
else:
   width = defaultWidth
   height = defaultHeight

if args.title is not None:
     title = args.title
else:
     title = defaultTitle


 
# Opens original image
original = Image.open(r"original.png")

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

# Create manifest.json
manifest = dict()
manifest = {
   "manifest_version": 2,
   "name": title,
   "description": "Created with: https://bpepitoneperez.com/ChromeImageThemeCreator/",
   "theme": {
      "colors": {
         "bookmark_text": [ 255, 255, 255 ],
         "frame": [ 0, 0, 0 ],
         "ntp_background": [ 10, 17, 27 ],
         "ntp_link": [ 255, 255, 255 ],
         "ntp_section_link": [ 255, 255, 255 ],
         "ntp_section_text": [ 10, 17, 27 ],
         "ntp_text": [ 0, 0, 0 ],
         "tab_background_text": [ 250, 250, 250 ],
         "tab_text": [ 255, 255, 255 ],
         "toolbar": [ 10, 17, 27 ]
      },
      "images": {
         "theme_frame": "frame.png",
         "theme_ntp_background": "bg.png",
         "theme_tab_background": "tab_background.png",
         "theme_toolbar": "toolbar.png"
      },
      "properties": {
         "frame_alignment": "top",
         "ntp_background_alignment": "bottom",
         "ntp_background_repeat": "no-repeat",
         "tab_background_alignment": "top",
         "toolbar_alignment": "top"
      },
      "tints": {
         "buttons": [ 0.8, 0.3333, 0.96 ]
      }
   },
   "update_url": "https://clients2.google.com/service/update2/crx",
   "version": "1.0"
}

with open("manifest.json", "w") as outfile:
    json.dump(manifest, outfile)

# Create ZIP
zf = zipfile.ZipFile(title + ".zip", "w")

zf.write("./manifest.json")
zf.write("./bg.png")
zf.write("./frame.png")
zf.write("./toolbar.png")
zf.write("./tab_background.png")
zf.close()

# Remove created images
os.remove("./manifest.json")
os.remove("./bg.png")
os.remove("./frame.png")
os.remove("./toolbar.png")
os.remove("./tab_background.png")

# Create Google Assets
storeIcon = original.resize((128, 128))
storeIcon.save("storeIcon.png")

screenshot = original.resize((1280, 800))
screenshot.save("screenshot.png")

smallPromoTile = original.resize((440, 280))
smallPromoTile.save("smallPromoTile.png")

marqueePromoTile = original.resize((1400, 560))
marqueePromoTile.save("marqueePromoTile.png")