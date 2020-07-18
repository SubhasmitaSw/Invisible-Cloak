import cv2

cap = cv2.VideoCapture(0) #accessing webcam else you can specify the video path as well

while cap.isOpened():
    ret, back = cap.read()# reading from the webcam

    if ret: #if my wencam works then it will execute

        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):  #wait to capture the screen

            cv2.imwrite('background.jpg', back) #save file as background image
            break

cap.release()
cv2.destroyAllWindows()    