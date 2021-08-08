# Importing Image class from PIL module
from PIL import Image
import cv2
def crop_img(filename):
    im = Image.open(filename)
    width, height = im.size
    left = 5
    top = (height / 4)-20
    right = 340
    bottom = 3 * height / 4 
    im1 = im.crop((left, top, right, bottom))
    #cv2.imwrite('Cropped_img.jpg', im1)
    im1.save("Cropped_Passport_img.png")
    im1.show()
    return "Cropped_Passport_img.png"

    

    