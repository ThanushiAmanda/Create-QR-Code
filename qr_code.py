import qrcode as qr
img = qr.make("https://youtu.be/YvKTjuqrmnA?si=ITV3_vQnTEcDrhRc")
img.save("Arduino_youtube.png")