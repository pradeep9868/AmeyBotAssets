# from urllib.request import urlopen
# from io import BytesIO
# from PIL import Image
import base64
import json
# ameyBotLogo = "https://raw.githubusercontent.com/Amey-Gurjar/AmeyBotAssets/main/ameyBotUpdater.png"
# image_byt = urlopen(ameyBotLogo).read()
# image_b64 = base64.encodebytes(image_byt)
# print(image_b64)
# img = Image.open(BytesIO(base64.b64decode(image_b64)))
# # img.show()

import requests
response = requests.get("https://github.com/Amey-Gurjar/AmeyBotAssets/raw/main/JSON/internalAmeyBotSetting.json", stream=True)
print(json.loads(response.content))