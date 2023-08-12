import qrcode
img = qrcode.make('https://www.debian.org/download')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")