from PIL import Image
import base64

image = Image.open("oxygen.png")

print(image.histogram())

print base64.b64encode(image)

print imageBytes.decode("utf-8")

data = image.getdata()
#for dataPoint in data:
	#print dataPoint