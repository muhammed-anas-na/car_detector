import cv2
trained_data = cv2.CascadeClassifier('cars.xml')
webcam = cv2.VideoCapture('Cars Moving On Road Stock Footage - Free Download.mp4')
while True:
    sucessfull_frame_read,frame = webcam.read()

    gray_scale_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = trained_data.detectMultiScale(gray_scale_image)


    for (x,y,w,h) in cars:
        cv2.rectangle(gray_scale_image,(x,y),(x+w,y+h),(0,0,225),2)

    cv2.imshow('webcam',gray_scale_image)


    key=cv2.waitKey(1)   
    if key==81 or key==113:
        break 

    
webcam.release()
print('Code completed')