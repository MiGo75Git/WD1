from PIL import Image

try:

    try:
        im_me2be = Image.open("C:/Users/miran/Desktop/Ninja/Lesson2/static/smart_ninja_logo.jpg")
    except IOError:
        print("Unable to load image NINJA")

    try:
        im_me = Image.open("C:/Users/miran/Desktop/Ninja/Lesson2/static/me.jpg")
    except IOError:
        print("Unable to load image ME")

    im_out = Image.new("RGB")
    im_out = Image.blend(im_me, im_me2be, 80)

except :
    print("Blending error")
    im_out = im_me2be

im_out.save("C:/Users/miran/Desktop/Ninja/Lesson2/static/show_them.png", format="PNG", quality=95)
