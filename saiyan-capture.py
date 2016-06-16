from core.parser import __parser__
from core.plugins import __modules__
from common.colors import red
from progress.bar import ShadyBar

import pyscreenshot as ImageGrab
import pytesseract
import time

try:
    import Image
except ImportError:
    from PIL import Image

objects = {}


def logo():
    print("""   ____     _
  / __/__ _(_)_ _____ ____
 _\ \/ _ `/ / // / _ `/ _ \

/___/\_,_/_/\_, /\_,_/_//_/
           /___/           """)


def process(data):
    if __parser__.url(data) is True:
        url_result = __modules__['print_url'].run(data)
        print "\t" + red("object found : ") + data + "\t" + red("url title : ") + url_result
        objects[data] = url_result

    elif __parser__.timestamp(data) is True:
        timestamp_result = __modules__[
            'print_timestamp'].run(data)
        print "\t" + red("UNIX timestamp converted : ") + timestamp_result
        # pass
    else:
        # print red(data + " not in patterns")
        pass

# print screen
img = ImageGrab.grab()
img.save('/tmp/test.jpg')

# get text from image
text = pytesseract.image_to_string(Image.open('/tmp/test.jpg'))
data = text.split(" ")

logo()
bar = ShadyBar('Saiyan Glass Processing', max=len(data))
for i in range(0, len(data) - 1):
    try:
        process(data[i].strip('\n'))
    except:
        print "\t" + "Unknown Objects found, Can't be processed."
    finally:
        bar.next()
    time.sleep(0.01)

bar.finish()


# print objects
