# Working with QR codes
import qrcode

# data input

data = "https://DesignIsOrion.com"

# output

filename = 'qr.png'


# generate qr code

img = qrcode.make(data)
img.save(filename)
