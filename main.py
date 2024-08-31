from PIL import Image, ImageDraw, ImageFont

im = Image.open("images/doom.png")
# test = Image.new('1', (im.width//2, im.height//2))
text = ImageFont.truetype("courbd.ttf", 6)
# im.show()
im = im.resize((im.width//8, im.height//8))
colorMap = list(im.getdata())
# im = im.resize((im.width*8, im.height*8))
im = im.convert('L')
# print(colorMap)
# test = test.convert('1')
# arr = str(test.tobitmap()).split(",")
# arr = str(im.tobitmap()).split(",")
arr = im.getdata()
dict = {'f' : ' ',
        'e' : '^',
        'd' : '+',
        'c' : '>',
        'b' : ')',
        'a' : 'i',
        '9' : 'j',
        '8' : '@',
        '7' : '$',
        '6' : 'G',
        '5' : 'D',
        '4' : 'A',
        '3' : 'W',
        '2' : 'M',
        '1' : 'N',
        '0' : '#',}
ascii = ""
idk = 0
enter = 0
arr = list(arr)
pic = Image.new('RGBA', (im.width*8, im.height*8), (255,255,255,255))
draw = ImageDraw.Draw(pic)
# for bit in arr:
#     print(bit)
#     temp = hex(bit)
#     if len(temp) == 3:
#         temp += "0"
#     print(temp)
#     temp = temp[-2:-1]
#     ascii += dict[temp]*2
#     # if bit[:2] == "\\n":
#     if idk %im.width == 0:
#         ascii += "\n"
#     idk += 1
# draw.text((0,0), ascii, font = text)

for bit in arr:
    temp = hex(bit)
    if len(temp) == 3:
        temp = temp[0:2] + "0" + temp[-1]
    temp = temp[-2:-1]
    if idk %im.width == 0:
        enter += 8
    draw.text(((idk)%im.width*8,enter), dict[temp]*2, font = text, fill = colorMap[idk])
    # if bit[:2] == "\\n":
    idk += 1

pic.show()

# TODO create new image using new image and text
# https://pillow.readthedocs.io/en/stable/reference/Image.html
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text