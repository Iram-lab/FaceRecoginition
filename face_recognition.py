from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

        #title
        title_lbl=Label(self.root,text="FACE RECOGNITION" ,font=("times new roman",35,"bold"),bg="lightblue", fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=47)

        #first image
        img_top=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\face_detector1.jpg")
        img_top=img_top.resize((650,710))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=650,height=660)

        #second image
        img_bottom=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\Iram.jpg")
        img_bottom=img_bottom.resize((650,660))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=50,width=650,height=660)

        #Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="brown", fg="black")
        b1_1.place(x=200,y=550,width=240,height=40)
    #______________attendances____________
    def mark_attendance(self,i,r,n,d):
        with open("iram.cvs","r+",newline="\n") as f:
            mydataList=f.readlines()
            name_list=[]
            for line in mydataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n  not in name_list) and(d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


            

    #____________face recoginition____________
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,miniNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feaatures=classifier.detectMultiScale(gray_image,scaleFactor,miniNeighbors)


            coords=[]

            for(x,y,w,h) in feaatures:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Test@1234" , database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select St_Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Rollno from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>77:
                    cv2.putText(img,f"Student_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Rollno:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coords=[x,y,w,h]
            return coords

        def recognize(img,clf,faceCascade):
            coords=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

            video_cap.release()
            cv2.destroyAllWindows()








if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()