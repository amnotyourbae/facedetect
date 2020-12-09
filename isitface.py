import cv2 as cv
imcap = cv.VideoCapture(0)
imcap.set(3, 640)
imcap.set(4, 480)
faceCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
while True:
    success, img = imcap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
        cv.putText(img, 'wajah ganteng', (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)
        cv.imshow('face detect nam do san', img)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
cap.release()
cv.destroyWindow('face detect nam do san')
