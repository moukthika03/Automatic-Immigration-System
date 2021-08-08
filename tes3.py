#Extracting details from passport -Step 1
import cv2 
import pytesseract
def extract_info(scan_file):
    img = cv2.imread(scan_file)
    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(img, config=custom_config)
    #print(pytesseract.image_to_string(img, config=custom_config))
