from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

        #title
        title_lbl=Label(self.root,text="HELP DESK" ,font=("times new roman",35,"bold"),bg="white", fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=47)

        #first image
        img_top=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\har.jpg")
        img_top=img_top.resize((1530,690))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=690)

        dev_lable=Label(f_lbl,text="Email:iram29naa@gmail.com",font=("times new roman",25,"bold"),bg="lightblue",fg="blue")
        dev_lable.place(x=400,y=5)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()