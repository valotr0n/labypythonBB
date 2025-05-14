from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import random

# Задание 1
image = Image.open('images.jpg')
cropImg = image.crop((100, 100, 400, 400))

draw = ImageDraw.Draw(cropImg)
font = ImageFont.truetype('arial.ttf', 20)
draw.text((50, 50), 'Stranger Things', fill='red', font=font)
draw.line([(50, 50), (200, 50)], fill='blue', width=3)

blurRegion = cropImg.filter(ImageFilter.GaussianBlur(10))
cropImg.paste(blurRegion, (150, 150))
cropImg.save('output.jpg')
cropImg.show()

# Задание 2
image2 = Image.open('images1.jpg')
fragment = image2.crop((100, 100, 300, 300))

resized = fragment.resize((fragment.width * 2, fragment.height * 2))
rotated = resized.rotate(45)
grayscale = rotated.convert('L')

resized.save('resized.jpg')
resized.show()
rotated.save('rotated.jpg')
rotated.show()
grayscale.save('grayscale.jpg')
grayscale.show()

# Задание 3
image3 = Image.open('images2.jpg')
width, height = image3.size

left = image3.crop((0, 0, width // 2, height))
right = image3.crop((width // 2, 0, width, height))

newImg = Image.new('RGB', (width, height))
newImg.paste(right, (0, 0))
newImg.paste(left, (width // 2, 0))

draw = ImageDraw.Draw(newImg)
draw.text((10, 10), 'МЕНЯЕМ МЕСТАМИ', fill='red')
newImg.save('swap.jpg')

# Задание 4
img1 = Image.open("images3.jpg")
img2 = Image.open("images4.jpg").filter(ImageFilter.BLUR)

resultImg = img1.copy()
rectArea = (100, 100, 400, 400)
resizedImg2 = img2.resize((rectArea[2] - rectArea[0], rectArea[3] - rectArea[1]))
resultImg.paste(resizedImg2, rectArea)
resultImg.save("result.jpg")

# Задание 5
image6 = Image.open('images5.jpg')
imgArr = np.array(image6)
imgEnd = Image.fromarray(imgArr + 50)
imgEnd.save('OperationImgae.jpg')

# Задание 6
images = [
    Image.open('images.jpg'),
    Image.open('images1.jpg'),
    Image.open('images2.jpg'),
    Image.open('images3.jpg')
]

size = (300, 300)
collage = Image.new('RGB', (size[0] * 2, size[1] * 2))

for i, img in enumerate(images):
    x = 0 if i % 2 == 0 else size[0]
    y = 0 if i < 2 else size[1]
    collage.paste(img.resize(size), (x, y))

collage.save('collage.jpg')

# Задание 7
images = {
    "собака": "dog.jpg",
    "кошка": "cat.jpg",
    "корова": "cow.jpg",
    "c++": "bb.jpg"
}

score = 0
for _ in range(4):
    name, file = random.choice(list(images.items()))
    Image.open(file).show()
    answer = input("Что на картинке? ").lower()

    if answer == name:
        print("Верно")
        score += 1
    else:
        print(f"Нет, это - {name}")

print(f"\nПравильных ответов: {score} из 4")