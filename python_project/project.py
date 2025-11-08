import qrcode

data = "https://cdn.britannica.com/23/256823-101-11E00D74/images/image-2.jpg"  # You can change this to any text or URL

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("white.png")

print("QR Code generated and saved as my_qrcode.png")