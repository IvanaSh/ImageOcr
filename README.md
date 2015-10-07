## **ImageOcr**##

ImageOcr is a simple library that reads text from an image and prints it as a string.

## **Requirements**##

To install the necessary requirements in order to use ImageOcr type:

* pip install -r requirements.txt
* sudo apt-get install tesseract-ocr

## **Usage**##

```
#!python
>>>import sys
>>>from imageocr import ImageOcr

>>>i = ImageOcr('test1.png')
>>>print i.to_string()

```
ABCDEFGHIJKLIVI
   NOPQRSTUVWXYZ