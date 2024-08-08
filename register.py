from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x710+0+0")


        #first image
        img=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\un.jpg")
        img=img.resize((1530,710))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=710)

        #second image
        img1=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\how.jpeg")
        img1=img1.resize((400,550))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=50,y=60,width=400,height=550)

        #main FRame
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=60,width=700,height=550)

        #labels
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        #First name
        first_label=Label(frame,text="First Name:",font=("times new roman",12,"bold"),bg="white")
        first_label.place(x=30,y=70)

        first_entry=ttk.Entry(frame,width=25,font=("times new roman",12,"bold"))
        first_entry.place(x=30,y=100)

        #Contact No
        No_label=Label(frame,text="Contact No:",font=("times new roman",12,"bold"),bg="white")
        No_label.place(x=30,y=130)

        No_entry=ttk.Entry(frame,width=25,font=("times new roman",12,"bold"))
        No_entry.place(x=30,y=160)

        #Question
        Q_label=Label(frame,text="Select Security Question:",font=("times new roman",12,"bold"),bg="white")
        Q_label.place(x=30,y=190)

        Q_entry=ttk.Entry(frame,width=25,font=("times new roman",12,"bold"))
        Q_entry.place(x=30,y=220)

        

        #Password
        pass_label=Label(frame,text="Set Password:",font=("times new roman",12,"bold"),bg="white")
        pass_label.place(x=30,y=250)

        pass_entry=ttk.Entry(frame,width=25,font=("times new roman",12,"bold"))
        pass_entry.place(x=30,y=280)





if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()