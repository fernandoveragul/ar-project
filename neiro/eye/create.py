import qrcode
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)
qr.add_data("https://docs.google.com/document/d/1NH59MkF3c3doDKbZ-6KPda09_ts5v8IlDKpDhHc5kWc/edit")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode6.jpg','JPEG')


