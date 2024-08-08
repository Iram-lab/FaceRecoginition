from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

        #title
        title_lbl=Label(self.root,text="DEVELOPER" ,font=("times new roman",35,"bold"),bg="white", fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=47)

        #first image
        img_top=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\dev.jpg")
        img_top=img_top.resize((1530,690))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=690)

        #main frame'
        main_farme=Frame(f_lbl,bd=2,bg="white")
        main_farme.place(x=800,y=0,width=500,height=500)

        #first image
        img_top1=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\kiran.jpg")
        img_top1=img_top1.resize((200,200))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_farme,image=self.photoimg_top1)
        f_lbl.place(x=250,y=0,width=200,height=200)

       #Developer
        dev_lable=Label(main_farme,text="hello my name,kiran",font=("times new roman",17,"bold"),bg="white")
        dev_lable.place(x=0,y=5)

        dev_lable=Label(main_farme,text="I am full stack developer",font=("times new roman",17,"bold"),bg="white")
        dev_lable.place(x=0,y=35)

        #second image
        img_top2=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\developer.jpg")
        img_top2=img_top2.resize((500,300))
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_farme,image=self.photoimg_top2)
        f_lbl.place(x=0,y=210,width=500,height=300)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()