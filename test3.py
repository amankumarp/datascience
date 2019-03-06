from PIL import ImageTk
import cv2,os
from tkinter import *
from tkinter import filedialog

global file

def tek_pic():
    global name2
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read();
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5);
        # eyes = eye.detectMultiScale(gray, 1.3, 5);
        if cv2.waitKey(100) == 13:
            file = filedialog.asksaveasfile(mode="w", defaultextension=".png",
                                                    filetypes=(("PNG File", ".png"), ("JPG File", "*.jpg")),initialdir=os.getcwd())
            name=file.name[::-1]
            t=name.find('/')
            name2=''
            for i in range(0,t):
                  name2=name2+name[i]
            name2=name2[::-1]

            cv2.imwrite(name2,frame)
            show()
            break;

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1);
            # sample = sample + 1;
            # cv2.imwrite("dataset\ " + name + "." + Id + '.' + str(sample) + ".jpg", gray[y:y + h, x:x + w])
        # for (e_x, e_y, e_w, e_h) in eyes:
        #     cv2.rectangle(frame, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0),1);
        cv2.imshow('image',frame)
    cam.release()
    cv2.destroyAllWindows()
def show():
    global name2
    photo.configure(file=name2)




root=Tk()
root.title('camera (made by Aman kumar) ')
topframe=Frame(root)

canvas = Canvas(topframe, height=480, width=640,)
photo = PhotoImage(file='')
draw_img = canvas.create_image(0, 0, image=photo, anchor=NW)
canvas.pack()

button=Button(root,text="Capture ",bg='blue',command=tek_pic)
button.pack(side=BOTTOM)
button1=Button(root,text="")
topframe.pack(side=TOP)
label=Label(root,text="information: made by amankumar ")
label.pack(side=TOP)
root.mainloop()
