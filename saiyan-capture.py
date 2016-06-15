from core.parser import __parser__
from core.plugins import __modules__
from common.colors import red

import pyscreenshot as ImageGrab
import pytesseract

try:
    import Image
except ImportError:
    from PIL import Image

objects = {}


def process(data):
    if __parser__.url(data) is True:
        url_result = __modules__['print_url'].run(data)
        print red("object found : ") + data
        print red("url title : ") + url_result
        objects[data] = url_result

    elif __parser__.timestamp(data) is True:
        # timestamp_result = __modules__[
            # 'print_timestamp'].run(data)
        # print timestamp_result
        pass
    else:
        # print red(data + " not in patterns")
        pass

# print screen
img = ImageGrab.grab()
img.save('/tmp/test.jpg')

# get text from image
text = pytesseract.image_to_string(Image.open('/tmp/test.jpg'))
data = text.split(" ")

for i in range(0, len(data) - 1):
    process(data[i].strip('\n'))


# print objects
