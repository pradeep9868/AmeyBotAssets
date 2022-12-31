from urllib.request import urlopen
import base64
ameyBotLogo = "https://raw.githubusercontent.com/Amey-Gurjar/AmeyBotAssets/26ac73ca387563a4bce388f108387ca1b0527e12/ameyBotUpdater.png"
image_byt = urlopen(ameyBotLogo).read()
print(image_byt)
image_b64 = base64.encodebytes(image_byt)
print(image_b64)