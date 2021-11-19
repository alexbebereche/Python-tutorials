import qrcode

img = qrcode.make('basic example')
img.save('basic_qr.png')