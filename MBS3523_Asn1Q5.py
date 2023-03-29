import cv2


def nothing(x):
    pass


cap = cv2.VideoCapture(0)


cv2.namedWindow('image')
cv2.createTrackbar('Vertical Line', 'image', 0, 640, nothing)
cv2.createTrackbar('Horizontal Line', 'image', 0, 480, nothing)

while True:

    ret, frame = cap.read()


    v_pos = cv2.getTrackbarPos('Vertical Line', 'image')
    h_pos = cv2.getTrackbarPos('Horizontal Line', 'image')


    cv2.line(frame, (v_pos, 0), (v_pos, 480), (0, 0, 255), 2)
    cv2.line(frame, (0, h_pos), (640, h_pos), (0, 0, 255), 2)


    cv2.imshow('image', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()