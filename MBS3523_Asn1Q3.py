import cv2

box_size = 80
box_speed = 5

cap = cv2.VideoCapture(0)

box_x = 0
box_y = 0
box_dx = box_speed
box_dy = box_speed
box_angle = 45

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) > 0:
        (x, y, w, h) = faces[0]

        box_x += box_dx
        box_y += box_dy
        if box_x < 0 or box_x + box_size > frame.shape[1]:
            box_dx = -box_dx
            box_x += box_dx
        if box_y < 0 or box_y + box_size > frame.shape[0]:
            box_dy = -box_dy
            box_y += box_dy

        cv2.rectangle(frame, (box_x, box_y), (box_x + box_size, box_y + box_size), (0, 0, 255), 2)
    else:

        box_x = int(frame.shape[1] / 2 - box_size / 2)
        box_y = int(frame.shape[0] / 2 - box_size / 2)
        box_dx = box_speed
        box_dy = box_speed
        box_angle = 45

    text = "MBS3523 Assignment 1b - Q3    Name: Lai Ho"
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = int(frame.shape[1] / 2 - text_size[0] / 2)
    cv2.putText(frame, text, (text_x, text_size[1]), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
