import pyqrcode
import png
from pyqrcode import QRCode

s = input('Enter the link: ')

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
name=input("Enter the name for qrcode to be saved: ")
url.png(f'{name}.png',scale = 6)
