# Ritesh Aasutoshs
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
from train import Train
from face_recognition import Face_Recognition
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Home:

    def __init__(self, root):
        self.root = root
#   self.root.geometry( "1920x1080+0+0" )
        self.root.geometry("1530x790+0+0")
        # Change the title to the name of software
        self.root.title("Recognition System")

        root.configure(bg="white")  # Set background color to white
        # Image-1

        img1 = Image.open(r"Image\home_title.png")  # Path of image
        img1 = img1.resize((1530, 150))  # Size of image
        self.img_1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.img_1)
        f_lbl.place(x=0, y=0, width=1530, height=150)  # position of image

        # Image-2 (Student Details)

        img2 = Image.open(r"Image\sd.png")  # Path of image
        img2 = img2.resize((238, 238))
        self.img_2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image=self.img_2, command=self.student_details,
                    borderwidth=0, background="White", activebackground="white", cursor="hand2")
        b1.place(x=555, y=215, width=238, height=238)

        # Image-3

        img3 = Image.open(r"Image\db.png")  # Path of image
        img3 = img3.resize((238, 238))
        self.img_3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.img_3, command=self.attendance_data,
                    borderwidth=0, background="White", activebackground="white", cursor="hand2")
        b1.place(x=889, y=215, width=238, height=238)

        # Image-4

        img4 = Image.open(r"Image\tr.png")  # Path of image
        img4 = img4.resize((238, 238))
        self.img_4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image=self.img_4, borderwidth=0, background="White",
                    activebackground="white", cursor="hand2", command=self.train_data)
        b1.place(x=1223, y=215, width=238, height=238)

        # Image-5

        img5 = Image.open(r"Image\photos.png")  # Path of image
        img5 = img5.resize((238, 238))
        self.img_5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image=self.img_5, command=self.open_img, borderwidth=0,
                    background="White", activebackground="white", cursor="hand2")
        b1.place(x=555, y=512, width=238, height=238)

        # Image-6

        img6 = Image.open(r"Image\dev.png")  # Path of image
        img6 = img6.resize((238, 238))
        self.img_6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image=self.img_6, command=self.developer_data,
                    borderwidth=0, background="White", activebackground="white", cursor="hand2")
        b1.place(x=889, y=512, width=238, height=238)

        # Image-7

        img7 = Image.open(r"Image\help.png")  # Path of image
        img7 = img7.resize((238, 238))
        self.img_7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root, image=self.img_7, command=self.help_data, borderwidth=0,
                    background="White", activebackground="white", cursor="hand2")
        b1.place(x=1223, y=512, width=238, height=238)

        # Attendance

        # image of button
        img_take_att = Image.open(r"Image\take_att2.png")  # Path of image
        img_take_att = img_take_att.resize((410, 536))  # Size of image
        self.img_std_button = ImageTk.PhotoImage(img_take_att)

        f_lbl = Label(self.root, image=self.img_std_button, bg="white")
        f_lbl.place(x=64, y=215, width=410, height=536)  # position of image

        # Take attendance blue botton

        img8 = Image.open(r"Image\take sttendance button.png")  # Path of image
        img8 = img8.resize((361, 82))
        self.img_8 = ImageTk.PhotoImage(img8)
        b1 = Button(self.root, image=self.img_8, command=self.face_data, borderwidth=0,
                    background="White", activebackground="white", cursor="hand2")
        b1.place(x=86, y=658, width=361, height=82)

#   b1_bottom=Button(text="Take Attendance",cursor="hand2",font=("lato",15,"bold"),bg="#2E75E9",fg="White",bd=-4,relief="sunken",activebackground="#2E75E9",)
#   b1_bottom.place(x=180,y=675)

    # ========== For Opening Photos Folder ==============

    def open_img(self):
        os.startfile("data")

        # =============== Function Buttons =============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

        # ============== Function Button for Train =============
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

        # ============== Function for Face Recognition =============
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

        # ============== Function for Attendance System =============
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

        # ============= Developers  Window ====================
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

        # ================ Help Desk =========================
    def help_data(self):

        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Home(root)
    root.mainloop()
