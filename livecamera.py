import cv2

vidio   = cv2.VideoCapture(0)

while True:
    cond, frame = vidio.read()
    # edge = cv2.Canny(frame, 50,50)
    cv2.imshow('Edge detect live video', frame)
    exit = cv2.waitKey(1) & 0xff

    if exit == ord('x'):
        break
cv2.destroyAllWindows()
vidio.release()
