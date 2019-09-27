# 生成图片验证码
# from PIL import Image,ImageFilter,ImageFont,ImageDraw
# import random
# # 1.随机生成字母
# def rndwords():
#     return chr(random.randint(65,90))
# # 2.随机生成背景点颜色
# def bgColor():
#     return (random.randint(64,255),random.randint(0,255),random.randint(64,255))
# # print(bgColor())
# # 3.随机生成字体颜色
# def wordColor():
#     return (random.randint(64, 255), random.randint(0, 255), random.randint(64, 255))
# # print(wordColor())
# height=60
# width=240
# # 创建画布
# image=Image.new("rgb",(width,height),(20,20,20))
# # 创建draw
# Draw=ImageDraw.Draw(image)
# # 创建字体
# font=ImageFont.truetype("字体地址",30)      #(字体地址，字号)
# # 填充每个像素
# for x in range(width):
#     for y in range(height):
#         Draw.point((x,y),fill=bgColor())
# # 输出字体
# for t in range(4):
#     Draw.text((60*t+10,10),rndwords(),fill=wordColor())
# # 模糊
# image.filter(ImageFilter.BLUR)
# image.save("code2.jpg","jpeg")

# 裁剪
# box=(100,100,200,200)
# image2=image1.crop(box)

# 水印
# image2.paste(image1,(100,100),None)
# image2.show()

# 旋转
# image.transpose(Image.ROTATE_180)
