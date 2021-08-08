import cv2
import time
def captureimg():

    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("test")
    time.sleep(4)
    img_counter = 1
    res=True
    while res==True:
        # Capturing the frame
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        #Frame is displayed for 2 seconds  
        k = cv2.waitKey(2000)
        img_name = "Immigration_{}.png".format(img_counter)
        # Saving image and giving name to it  
        cv2.imwrite(img_name, frame)
        print("Picture clicked successfully!! Please wait while we process....")
        res=False

    cam.release()

    cv2.waitKey(1)
    cv2.destroyAllWindows()
    for i in range (1,5):
        cv2.waitKey(1)
    return img_name

