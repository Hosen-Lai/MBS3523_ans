import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('Color', cv2.WINDOW_NORMAL)
cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Color', frame)
    cv2.imshow('Grayscale', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

