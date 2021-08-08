#Facial recognition- Step2
#import face_recognition
from PIL import Image
import imagehash

def check_sim(pass_image,image):
    hash0 = imagehash.average_hash(Image.open(pass_image)) 
    hash1 = imagehash.average_hash(Image.open(image)) 
    cutoff = 5

    if hash0 - hash1 < cutoff:
        return 'Thank you, have a nice journey!'
    else:
        return 'Faces do not seem to match!! Please ask for assistance..'