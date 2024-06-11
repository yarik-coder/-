import cv2
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import os
from PIL import Image, ImageChops

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def cutter(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(res)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces: #находим лицо
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) #обводим лицо
        im = Image.open(res)
        im_crop = im.crop((x, y, x + w, y + h)) #обрезаем лицо
        im_crop.save('pon.png', quality=95) #сохраняем
        cv2.imshow('img', img)
class Cam:
    def __init__(self, master=None):
        self.cap = cv2.VideoCapture(0) #подключчаемся к камере
        self.master = master
        self.canvas = Canvas(master, width=800, height=600) #создаём канвас для изображение с камеры
        self.canvas.pack()
        self.btn = Button(root, text="регистрация", command=self.photo) #создаём кнопку
        self.btn.pack()

        self.delay = int(1000/self.cap.get(cv2.CAP_PROP_FPS)) #получаем картинку с камеры и обнавляем её
        self.update()

    def photo(self):
        ret, img = self.cap.read()
        global res
        res = format(txt.get())
        res = "photo/" + res + ".png"
        if ret:
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces: #находим лица
                cv2.rectangle(frame, (x, y), (x + w, y + h), (250, 0, 0), 2)
                im = Image.fromarray(frame)
                im_crop = im.crop((x, y, x + w, y + h)) #обрезаем
                im_crop.save(res, quality=95) #сохраняем
    def update(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Сохранение картинки
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #серый
            faces = face_cascade.detectMultiScale(gray, 1.3, 5) #ищем лица по наст а не по цыклу
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) #Создается прямоугольник
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
            self.master.after(self.delay, self.update)
        else:
            self.cap.release()


# noinspection PyTypeChecker
def procent(Cam):
    global im_crop, b
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    ret, img = Cam.cap.read()
    if ret:
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:  # находим лица
            cv2.rectangle(frame, (x, y), (x + w, y + h), (250, 0, 0), 2)
            im = Image.fromarray(frame)
            im_crop = im.crop((x, y, x + w, y + h))  # обрезаем
        photo = os.listdir("photo")
        print(photo)
        b = 0
        x = 0
        for i in photo:
            image_1 = im_crop
            image_2 = Image.open("photo/" + i)
            result = ImageChops.difference(image_1, image_2)
            f = 0
            test = np.array(result)
            test1 = test.shape[0]
            test2 = test.shape[1]
            size = test1 * test2
            for i in test:
                for j in i:
                    if j[0] < 50 and j[1] < 50 and j[2] < 50:
                        f += 1
                    else:
                        continue

            xx = x
            x = 100 * f // size
            print(x)
            b = str(b) + " " + str(xx)
            e = 0
            print(len(photo))
            for i in photo:
                e = e + 1
                if e == len(photo) // 2:
                    b = b + " " + str(x)
            print(b)






if __name__ == "__main__":
    root = Tk()
    root.title('слежка')
    camera = Cam(master=root)
    txt = Entry(root, width=10)
    txt.place(relx = 0.5, rely = 0.3)
    txt.pack()
    but = Button(root, text="проверка в процентовке", command= lambda: procent(camera))
    but.pack()

    root.mainloop()