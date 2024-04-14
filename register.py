from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib
import ctypes

background="#06283D"
framebg="EDEDED"
framefg="06283D"

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root=Tk()
root.title("Image Stegano System - Add User")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def register():
    username=user.get()
    password=code.get()
    admincode=adminaccess.get()
    ###print(username,password,admincode) >>>>>>utk cekk je
    if admincode=="908890":

        if(username=="" or username=="New UserID") or (password=="" or password=="New Password"):
            messagebox.showerror("Entry Error!!", "Type UserID and Password!!")
        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',password='Nhafiz00_',database='fyp')
                mycursor=mydb.cursor()
                print("Yeayy Connected!!")
            
            except:
                messagebox.showerror("Connection","Database connection not stablish!!")

            try:
                command="create database fyp"
                mycursor.execute(command)

                command="use fyp"
                mycursor.execute(command)

                command="create table login(user int auto_increment key not null, Username varchar(50),Password varchar(100))"
                mycursor.execute(command)

            except:
                mycursor.execute("use fyp")
                mydb=mysql.connector.connect(host='localhost',user='root',password='Nhafiz00_',database='fyp')
                mycursor=mydb.cursor()

                hashed_password = hash_password(password)  # Hash the password

                command="insert into login(Username,Password) values(%s,%s)"
                mycursor.execute(command,(username,hashed_password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register","New User added Successfully!!!")
            

    else:
        messagebox.showerror("Admin Code!!", "Input the correct Admin Code to proceed!!")
   

    
def login():
    root.destroy()
    import LaisaDuoSteg
    

####background image
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="image/2.png")
Label(frame,image=backgroundimage).pack()

adminaccess=Entry(frame,width=7,fg="#000",border=0,bg="#e8ecf7",font=("Arial Bold",20),show="*")
adminaccess.focus()
adminaccess.place(x=527,y=267)

#####################User Entry
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    if user.get()=='':
        user.insert(0,'UserID')

user=Entry(frame,width=15,fg="#fff",border=0,bg="#375174",font=("Arial Bold",20))
user.insert(0,"New UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500,y=333)

########password entry#############################
def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code=Entry(frame,width=15,fg="#fff",border=0,bg="#375174", font=('Arial Bold',20))
code.insert(0,' New Password')
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=495,y=433)

#############Hide and show button##########################
button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True

openeye=PhotoImage(file="image/openeye.png")
closeeye=PhotoImage(file="image/closeeye.png")
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=740,y=439)

##########################################################
###########LOGIN BUTTON###################################

regis_button=Button(root,text="ADD USER",bg="#488FF7",fg="white",width=12,height=1,font=("Archivo Black",16,'bold'),bd=0,command=register)
regis_button.place(x=515,y=540)

backbuttonimage=PhotoImage(file="image/back.png")
BackButton=Button(root,image=backbuttonimage,bg="#15D9D3",bd=0,command=login)
BackButton.place(x=16,y=15)


#####################################################################################
root.mainloop()
