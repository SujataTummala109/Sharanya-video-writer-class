
import cv2

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("Unable to read teh feed")
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

fps = int(vid.get(cv2.CAP_PROP_FPS))
print("height: " ,height, "width: ", width, "fps :", fps)

out = cv2.VideoWriter('Boxing1.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while True:

    ret, frame = vid.read()
    cv2.imshow("Web Cam", frame)

    if cv2.waitKey(25):
        break
vid.release()
out.release()
cv2.destroyAllWindows()