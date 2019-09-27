from PIL import Image, ImageDraw, ImageFont, ImageFilter

# im = Image.open('image/hot4.jpg')
# # 获得图像尺寸:
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
#
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# im.save('image/hot5.jpg', 'jpeg')
# print(im.size)
# a=im.size[0]
# print(a)
# print(type(im.size))


# 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('image/hot4.jpg')
# # 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('image/hot6.jpg', 'jpeg')


# import random
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))      #大写字母
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('image/code2.jpg', 'jpeg')

# region = Image.open("image/hot4.jpg")
# im = Image.open("image/code.jpg")
# im.paste(region,(100,100),None)
# im.show()

# im = Image.open("image/hot4.jpg")
# box = (0,0,200,200)
# region = im.crop(box)
# region.show()

# im = Image.open("image/hot4.jpg")
# im_rotate_180 = im.transpose(Image.ROTATE_180)
# im_rotate_180.show()
#
# im = Image.open("image/hot4.jpg")
# im_rotate_180 = im.transpose(Image.ROTATE_180)
# im_rotate_180.show()






