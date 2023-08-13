import qrcode
img = qrcode.make('https://genshin.hoyoverse.com/zh-tw/')
type(img)  # qrcode.image.pil.PilImage
img.save("genshin_start.png")