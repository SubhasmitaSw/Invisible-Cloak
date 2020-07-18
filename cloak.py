import cv2
import numpy as np # using numpy to store images as numpy treats image frames as arrays

cap = cv2.VideoCapture(0)
back = cv2.imread('./background.jpg')

while cap.isOpened():

    ret, frame = cap.read()#take each frame

    if ret:
        """now since every image is a composition of three
        colors RGB and here in this project we are going to eliminate one particular colour to make it look invisible
        therefore we have to convert the rgb into hsv format i.e is hue saturation value using which the particular colour will be identified and
        we can play around with it's saturation, intensity etc"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv", hsv)

    orange = np.uint8([[[0, 0, 255]]]) #bgr value of orange

    hsv_orange = cv2.cvtColor(orange, cv2.COLOR_BGR2HSV)

    #print(hsv_orange) gettig=ng hsv values of orange

    #lower range

    l_orange = np.array([0, 120, 70])
    u_orange = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, l_orange, u_orange)

    #upper range

    l_orange = np.array([170, 120, 70])
    u_orange = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, l_orange, u_orange)

    mask = mask1+mask2


    #mask = cv2.inRange(hsv, l_orange, u_orange)
    #cv2.imshow("mask", mask)

    part1 = cv2.bitwise_and(back, back, mask=mask)
    #cv2.imshow("part1", part1)

    mask = cv2.bitwise_not(mask)


    part2 = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("cloak", part1+part2)



    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cap.destroyAllWindows()                  