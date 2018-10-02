from PIL import Image, ImageFilter

def average_luminosity(patch, size):
    total_luminosity = 0
    for y in range(0,size):
        for x in range(0,size):
            patch = patch.convert('L')
            l = patch.getpixel((x,y))
            total_luminosity += l
    average_luminosity = total_luminosity/(size**2)
    return average_luminosity


im = Image.open("mario.jpg")
print(im.show())

im = im.resize((360, 360))
print(im.show())

im = im.filter(ImageFilter.FIND_EDGES)
print(im.show())

size = 10
patch_list=[]

for y in range(0,360,size):
    for x in range(0,360,size):
        box = (x,y,x+size,y+size)
        patch = im.crop(box)
        patch_list.append(patch)

output_string = ""

for Patch in patch_list:
    if average_luminosity(Patch, size) > 20:
        output_string = output_string + "@@"
    else:
        output_string = output_string + "  "
    if len(output_string) == 720/size:
        print(output_string)
        output_string = ""
