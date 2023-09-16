import qrcode
img = qrcode.make('https://hong539.github.io/resume/yh_resume.html')
type(img)  # qrcode.image.pil.PilImage
img.save("my_resume.png")