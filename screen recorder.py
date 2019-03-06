import cv2.data
import numpy as np
from PIL import ImageGrab


cam=cv2.VideoWriter('myscreen.mp4v',cv2.VideoWriter_fourcc(*'MPEG'),5.0,(1280,800))
# it is first code for screen reading
while True:
    prints=ImageGrab.grab()  #it function is send live screen as video streem
    n=np.array(prints)
    # print(prints)
    im=cv2.cvtColor(n,cv2.COLOR_BGR2RGB)
    cv2.imshow('window',im)
    cam.write(im)

    if cv2.waitKey(1)==13:
        break
cam.release()
cv2.destroyAllWindows()
