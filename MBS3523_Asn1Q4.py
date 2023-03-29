import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)


font = cv2.FONT_HERSHEY_SIMPLEX
text = 'MBS3523 Assignment 1c - Q4   Name: Lai Ho'
text_size = cv2.getTextSize(text, font, 1, 2)[0]
text_x = int((cap.get(3) - text_size[0]) / 2)
text_y = text_size[1] + 10

while True:


    ret, frame = cap.read()



    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    for (x, y, w, h) in faces:
        # 绘制矩形框
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        face_roi = frame[y:y+h, x:x+w]


        gray = cv2.cvtColor(frame[:y, :, :], cv2.COLOR_BGR2GRAY)
        frame[:y, :, :] = cv2.merge([gray, gray, gray])

        gray = cv2.cvtColor(frame[y+h:, :, :], cv2.COLOR_BGR2GRAY)
        frame[y+h:, :, :] = cv2.merge([gray, gray, gray])

        gray = cv2.cvtColor(frame[:, :x, :], cv2.COLOR_BGR2GRAY)
        frame[:, :x, :] = cv2.merge([gray, gray, gray])

        gray = cv2.cvtColor(frame[:, x+w:, :], cv2.COLOR_BGR2GRAY)
        frame[:, x+w:, :] = cv2.merge([gray, gray, gray])






        cv2.putText(frame, text, (text_x, text_y), font, 1, (0, 0, 255), 2)


    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

