from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x710+0+0")

        #first image
        img=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\Stanford.jpg")
        img=img.resize((1530,710))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=710)

        #FRame
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=50,width=400,height=500)
        # login image
        img1=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\LoginIconAppl.png")
        img1=img1.resize((100,100))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(frame,image=self.photoimg1)
        f_lbl.place(x=130,y=20,width=120,height=120)

        get_start=Label(frame,text="Get Started",font=("times new roman",27,"bold"),fg="white",bg="black")
        get_start.place(x=100,y=150)

        #username
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=90,y=220)

        self.username=ttk.Entry(frame,width=30,font=("times new roman",12,"bold"))
        self.username.place(x=70,y=250)

        # user image
        img2=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\user.jpeg")
        img2=img2.resize((22,22))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(frame,image=self.photoimg2,bg="red",fg="white")
        f_lbl.place(x=70,y=220,width=22,height=22)

        #password
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=90,y=300)

        self.password=ttk.Entry(frame,width=30,font=("times new roman",12,"bold"))
        self.password.place(x=70,y=325)

        #password image
        img3=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\lock.jpeg")
        img3=img3.resize((22,22))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(frame,image=self.photoimg3,bg="red",fg="white")
        f_lbl.place(x=70,y=300,width=22,height=22)

        #login button
        loginbtn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=130,y=360,width=120,height=35)

        #resigter button
        registerbtn=Button(frame,text="Create New Account",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=25,y=410,width=200,height=30)

        #forgot button
        loginbtn=Button(frame,text="forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=25,y=440,width=200,height=30)

    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.username.get()=="kapu" and self.password.get()=="ashu":
            messagebox.showinfo("Success","Welcome in project",parent=self.root)
        else:
            messagebox.showerror("Invalid","Invalid Username and Password",parent=self.root)
    

        
        

    












if __name__ == "__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()


        