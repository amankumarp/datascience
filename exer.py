import cv2,time

vid=cv2.VideoCapture('rr.mp4')
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    ret,frame=vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('image',frame)

    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
