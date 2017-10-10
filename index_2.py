#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pytesseract
from PIL import Image

image = Image.open('result_1.png')
#image = open("code.png")
colors = image.getcolors()
# print colors
code = pytesseract.image_to_string(image)
print code