from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename,asksaveasfilename,askdirectory 
from PIL import Image,ImageDraw,ImageFont,ImageTk,ImageColor
import io
import random
import webbrowser
import qrcode



root = Tk()
root.minsize(520, 400)
root.configure(background="#FA9900")
try:
   root.iconbitmap("icon.ico")
except:
    pass


def OpenFile():
    
    
    try:
       qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5

	)
       e1 = entry.get()
       data=e1
       qr.add_data(data)
       qr.make(fit=True)
       img=qr.make_image(fill="black",back_color="white")
       c = askdirectory(initialdir="C:/Users/../Desktop")      
       e2 = entry2.get()
       if e2!="":
          img.save(c+"/"+e2+".png")
       else:
          d = str(random.randint(1,123456789))
          img.save(c+"/"+d+".png")    
       w = Message(root, text="Successful",width=80)
       w.place(x=280, y=340, anchor="center")
       entry.delete(0, END)
 

    except:
        print("No file exists")

Title = root.title( "1001-QR-Generator")
label_pan = Label(root, text="Enter your (text , url ,...):",font="time 18"
                  ,background="#FA9900", foreground="#003300").place(x=220, y=20, anchor="center")

entry = Entry(root,font="time 24")
entry.place(x=220, y=70, anchor="center")

label_pan = Label(root, text="QR name ",font="time 24"
                  ,background="#FA9900", foreground="#003300").place(x=220, y=120, anchor="center")

entry2 = Entry(root,font="time 24")
entry2.place(x=220, y=160, anchor="center")




menu = Menu(root)
root.config(menu=menu)

def callback():
        webbrowser.open_new(r"https://www.facebook.com/massinissa.ziri.7")

button = Button(root, text="Generate", width=30, command=OpenFile)
button.place(x=220, y=220, anchor="center")

label_pan1 = Label(root, text="البرنامج صمم هدية لمجموعات ألف ليلة و ليلة",font="time 18"
                  ,background="#FA9900", foreground="green").place(x=20, y=260, anchor="w")
label_pan2 = Label(root, text="البرنامج مجاني لكل الاستعمالات فقد دعوة خير ",font="time 14"
                  ,background="#FA9900", foreground="black").place(x=40, y=290, anchor="w")

label_pan6 = Label(root, text="MADE BY \u00A9",font="time 14"
                  ,background="#FA9900", foreground="#CC0000").place(x=40, y=380, anchor="w")

button3 = Button(root, text="B.LOTFI", width=15, command=callback).place(x=200, y=380, anchor="center")

button1 = Button(root, text="Exit", command=root.destroy)
button1.place(x=460, y=380, anchor="center")


root.mainloop()


