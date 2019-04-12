
import requests
import pytesseract

try:
    import Image
except ImportError:
    from PIL import Image


TEST_CAPTCHA_IMAGE_URL = "https://incorp.interpark.com/captcha.do?_method=service"
CAPTCHA_FILE_NAME = "test.png"

img = Image.open(CAPTCHA_FILE_NAME)
new_size = tuple(2*x for x in img.size)
img = img.resize(new_size, Image.ANTIALIAS)
print(pytesseract.image_to_string(img))


