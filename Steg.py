from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root=Tk()
root.title("Image Stegano System")
root.geometry("1250x700+210+100")
root.resizable(False,False)
root.configure(bg="#2f4155")

##############Def untuk Image Processing######################
def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG file","*.jpg"),
                                                  ("All file","*.txt")))
    img = Image.open(filename)
    # Resize image to fit label dimensions
    img = img.resize((750, 650))
    img = ImageTk.PhotoImage(img)
    lb.configure(image=img, width=750, height=650)
    lb.image = img
    
    ##img=Image.open(filename)
    ##img=ImageTk.PhotoImage(img)
    ## lb.configure(image=img,width=250,height=250)
    ## lb.image=img

    
###########STEGANOGRAPHY##################################

def clear_text():
    text1.delete(1.0, END)
    
def hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)
    if secret:
        messagebox.showinfo("Success", "Message hidden successfully")
    
def show():
    ##clear_message=lsb.reveal(filename)
    ##text1.delete(1.0,END)
    ##text1.insert(END, clear_message)
    ##if clear_message:
    ## messagebox.showinfo("Success", "Message extracted successfully")
     try:
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
        text1.insert(END, clear_message)
        messagebox.showinfo("Success", "Message extracted successfully")
     except IndexError:
        messagebox.showwarning("No Message", "No message found in the image.")
    
def save():
    secret.save("stego.png")
    messagebox.showinfo("Success", "Image saved as stego.png successfully")


##First Frame##
frame1=Frame(root,bd=3,bg="black",width=780,height=680,relief=GROOVE)
frame1.place(x=10,y=10)

lb=Label(frame1,bg="black")
lb.place(x=10,y=10,width=780,height=680)

##Second Frame##
frame2=Frame(root,bd=3,bg="white",width=440,height=280,relief=GROOVE)
frame2.place(x=810,y=10)

#lb2=Label(frame2,bg="white")
#lb2.place(x=40,y=10)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.xview)
text1.configure(xscrollcommand=scrollbar1.set)


##Third Frame##
frame3=Frame(root,bd=3,bg="#2f4155",width=430,height=100,relief=GROOVE)
frame3.place(x=810,y=390)

Button(frame3,text="Open Image", width=12,height=1,font="arial 14 bold",command=showimage).place(x=20,y=35)
Button(frame3,text="Save Image", width=12,height=1,font="arial 14 bold",command=save).place(x=220,y=35)
Label(frame3,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=50,y=5)

##Fourth Frame##
frame4=Frame(root,bd=3,bg="#2f4155",width=430,height=160,relief=GROOVE)
frame4.place(x=810,y=490)

Button(frame4,text="Embed", width=12,height=1,font="arial 14 bold",command=hide).place(x=20,y=35)
Button(frame4,text="Extract", width=12,height=1,font="arial 14 bold",command=show).place(x=220,y=35)
Button(frame4,text="Clear", width=12,height=1,font="arial 14 bold",command=clear_text).place(x=20,y=105)

Label(frame4,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=50,y=5)


root.mainloop()
