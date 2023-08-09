import cv2
import numpy as np
import argparse as arg


parser= arg.ArgumentParser()
parser.add_argument("filter1", nargs='?')
parser.add_argument("filter2" , nargs='?')
parser.add_argument("filter3", nargs='?')
par= parser.parse_args()

list=[]
for i in range(1, 4):
    c= "par.filter" + str(i)
    c= eval(c)
    list.append(c)

gscaleOn= True if 'greyscale' in list else False
eDetectOn= True if 'edge-detection' in list else False
blurOn= True if 'blur' in list else False

vid= cv2.VideoCapture(0)


while True:
    
    bol, frame = vid.read()

    # used for monitoring keyboard keys
    key= cv2.waitKey(1)

    # greyscale code
    if key == ord('g'):
        gscaleOn= not gscaleOn

    if gscaleOn:
        frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    

    #edge detection code
    if key == ord('e'): 
        eDetectOn= not eDetectOn

    if eDetectOn:
        blur= cv2.blur(frame, (7,7))
        med= np.median(blur)
        lower= int(max(0,0.7*med))
        upper= int(min(255,0.7*med))
        frame = cv2.Canny(frame, lower, upper+75)
    

    #blur filter code
    if key == ord('b'):
        blurOn= not blurOn

    if blurOn:
        frame= cv2.blur(frame, (5,5))

        
    # Display the resulting frame
    cv2.imshow('Video', frame)

    # quits the program
    if key == ord('q'):
        break


# When everything is done, release the capture
vid.release()
cv2.destroyAllWindows()
