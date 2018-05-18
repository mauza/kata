# Extract jpg's from pdf's. Quick and dirty.
import sys

pdf = open(sys.argv[1], "rb").read()

startmark = b"\xff\xd8"
endmark = b"\xff\xd9"

istart = pdf.find(startmark)
iend = pdf.find(endmark)
jpg = pdf[istart:iend]
jpgfile = open("test.jpg", "wb")
jpgfile.write(jpg)
jpgfile.close()
