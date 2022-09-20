from PIL import Image
import os
for filename in str(os.listdir('img')).splitlines():
    filename = filename.split(' ')
    # image = Image.open('img/'+filename)
    # img = image.resize((640, 360), Image.ANTIALIAS)
    # img.save('img_1/'+filename, quality=50)
    print(filename)
