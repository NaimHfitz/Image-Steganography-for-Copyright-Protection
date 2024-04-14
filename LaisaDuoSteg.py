from tkinter import *
from tkinter import messagebox
import mysql.connector
import ctypes
import hashlib



background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

global attemp_no
attemp_no=0
def attemp():
    global attemp_no

    attemp_no+=1
    #print("No of Attempt is", attemp_no)
    if attemp_no==2:
        messagebox.showwarning("WARNING!", "You have reached Login attempt limit")
        root.destroy()
        
def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
    

def loginuser():
    username=user.get()
    password=code.get()

    if(username=="" or username=="UserID") or (password=="" or password=="Password"):
        messagebox.showerror("ERROR","Please fill in ID and Password")

    else:
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',password='Nhafiz00_',database='fyp')
            mycursor=mydb.cursor()
            #print("Yeayy Connected!!")
            
        except:
            messagebox.showerror("Connection","Database connection not stablish!!")
            return

        command="use fyp"
        mycursor.execute(command)

        command="select * from login where Username=%s"
        mycursor.execute(command,(username,))
        myresult=mycursor.fetchone()
        print(myresult)

        if myresult==None:
            messagebox.showinfo("Invalid","Invalid ID and Password!!")
            attemp()
        else:
            hashed_password_from_db = myresult[2]  # Assuming password is stored in the third column
            hashed_password_input = hash_password(password)

            if hashed_password_input == hashed_password_from_db:
                messagebox.showinfo("Login", "Successfully Login!!")
                root.destroy()
                import Steg
            else:
                messagebox.showinfo("Invalid", "Invalid ID and Password!!")
                attemp()
        ##else:
            ##messagebox.showinfo("Login","Successfully Login!!")
            ##root.destroy()
            ##import Steg

ctypes.windll.shcore.SetProcessDpiAwareness(1)        

root=Tk()
root.title("Image Stegano System - Login")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)

def registerPage():
    root.destroy()
    import register



####################background image#######################
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="image/login2.png")
Label(frame,image=backgroundimage).pack()

########user entry##############################
def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    if user.get()=='':
        user.insert(0,'UserID')

user=Entry(frame,width=10,fg="#fff",border=0,bg="#375174", font=('Arial Bold',24))
user.insert(0,'UserID')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=486,y=287)

########password entry#############################
def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code=Entry(frame,width=10,fg="#fff",border=0,bg="#375174", font=('Arial Bold',24))
code.insert(0,'Password')
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=486,y=390)

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
eyeButton.place(x=750,y=398)

##########################################################
###########LOGIN BUTTON###################################

loginButton=Button(root,text="LOGIN",bg="#488FF7",fg="white",width=10,height=1,font=("arial",16,'bold'),bd=0,command=loginuser)
loginButton.place(x=535,y=535)

label=Label(root,text="Want to add new user?",fg="#000000",bg="#DBDBDB",font=('Microsoft YaHei UI Light',9))
label.place(x=490,y=450)

registerButton=Button(root,text="Add user",border=0,bg="#DBDBDB",cursor='hand2',fg="#000000",command=registerPage)
registerButton.place(x=670,y=450)

root.mainloop()
