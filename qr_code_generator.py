import qrcode

data = input("Enter URL: ").strip()
filename = input("Enter File Name: ").strip()
filename = filename + ".png"
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR Code Saved {filename}")
