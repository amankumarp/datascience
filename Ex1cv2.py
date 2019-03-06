import cv2
import numpy as np
from PIL import ImageGrab


# it is first code for screen reading
while True:
    prints=ImageGrab.grab(bbox=(0,40,800,640))  #it function is send live screen as video streem
    n=np.array(prints)
    #im=cv2.cvtColor(n,cv2.COLOR_BGR2RGB)
    cv2.imshow('window',n)
    if cv2.waitKey(1)==13:
        cv2.destroyAllWindows()
        break
