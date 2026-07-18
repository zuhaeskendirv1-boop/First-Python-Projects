import qrcode
import qrcode.image.svg
from qrcode.image.pure import PyPNGImage

url = input("Enter a Url that you want to convert: ")
name = input("Enter a file name: ")
# img = qrcode.make(url, image_factory=PyPNGImage)

qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(url)
image = qr.make_image(fill_color='red', back_color='black')
image.save(name + ".png")


# img.save(name + ".png")