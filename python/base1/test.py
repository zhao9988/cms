import qrcode
from PIL import Image
import matplotlib.pyplot as plt


def getQRcode(strs, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    # 添加数据
    qr.add_data(strs)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="blue", back_color="white")
    # 添加logo
    icon = Image.open("logo.png")
    # 获取图片的宽高
    img_w, img_h = img.size
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)
    # 显示图片
    plt.imshow(img)
    plt.show()
    img.save(name)
    return img


if __name__ == '__main__':
    getQRcode("https://www.baidu.com/?tn=18029102_2_dg", "code.png")


















