from PIL import Image, ImageEnhance,ImageFilter
import os

path ="img"
pathOut = 'editedImgs'

for filename in os.listdir(path):
    # Open image and convert to RGB to avoid palette mode issues
    img = Image.open(f"{path}/{filename}").convert("RGB")
    edit= img.filter(ImageFilter.SMOOTH).convert("RGB")
    edit =img.filter(ImageFilter.SHARPEN).convert("L").rotate(0)

    factor =1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name =os.path.splitext(filename)[0]
    edit.save(f"{pathOut}/{clean_name}_edited.png", "png")

