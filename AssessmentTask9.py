from PIL import Image, ImageOps
image = Image.open('./img/avatars.png')
print(type(image))
print(image.size)
print(image.mode)
print(image.format)

width, height = image.size
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4

croppedImage = image.crop((left, top, right, bottom))

croppedImage.show()

croppedImage = croppedImage.rotate(180);

croppedImage.show()

croppedImage = ImageOps.mirror(croppedImage)

croppedImage.show()