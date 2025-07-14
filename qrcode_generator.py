"""
    qr code generator
    """

from qrcode import QRCode

website = input("Enter a website URL: ").strip()
file = input("Enter the filename: ").strip()


qr = QRCode(box_size="20", border="10")
qr.add_data(website)
image = qr.make_image(fill_color="black", background_color="white")
image.save(file)
print(f"QR code saved as {file}")
