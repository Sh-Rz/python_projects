import pyqrcode
import png
from pyqrcode import QRCode

s = 'https://github.com/Sh-Rz/python_projects'

url = pyqrcode.create(s)

url.png('QR.png', scale = 10)
