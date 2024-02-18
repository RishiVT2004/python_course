# install libraries
# create a func that collectes text and convert it to qr code
# save qr as a image
# run the func()

import qrcode


def gen_QR(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
        error_correction=qrcode.ERROR_CORRECT_L,

    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save("QRimg.png")


url = input('enter the url of site whose QR is needed : ')
gen_QR(url)
