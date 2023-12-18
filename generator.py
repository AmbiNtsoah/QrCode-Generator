from tkinter import *
import qrcode, PIL
from PIL import ImageTk
from tkinter import messagebox, filedialog

""" INITIALIZATION """
window = Tk()
window.title("QrCode Generator")
window.config(bg="gray")
window.geometry("400x500")
window.resizable(0,0)
icon = PhotoImage(file="images/unnamed.png")
window.iconphoto(False,icon)


""" CONTENT """

""" FONCTIONALITIES """
def createQR(*args):
    data = enter.get()

    if data:
        code = qrcode.make(data)
        ImageCode = code.resize((380,290))
        Image = ImageTk.PhotoImage(ImageCode)
        canvaa.delete("all")
        canvaa.create_image(0,0,anchor=NW, image= Image)
        canvaa.image = Image


def saveQR(*args):
    data = enter.get()

    if data:
        code = qrcode.make(data)
        ImageCode = code.resize((380,290))
        
        route = filedialog.asksaveasfilename(defaultextension=".png")
        if route:
            ImageCode.save(route)
            messagebox.showinfo("SUCCES", "QrCode saved Succesfully")
    else:
        messagebox.showwarning("FATAL ERROR","Enter a data first")






""" INTERFACE """

zone1 = Frame(window, bd=2, relief=RAISED)
zone1.place(x=10, y=5, width=380, height=385)

zone2 = Frame(window, bd=2, relief=SUNKEN)
zone2.place(x=10, y=405, width=380, height=80)

ImageCover = PhotoImage(file="images/cover.png")
#ImageCover.resize((380,390))

canvaa = Canvas(zone1)
canvaa.create_image(0,0,anchor=NW, image=ImageCover)
canvaa.image = ImageCover
canvaa.bind("<Double-1>", saveQR)
canvaa.pack(fill=BOTH)

enter = Entry(zone2, width=40, font=("Robotto", 12), justify=CENTER)
enter.bind("<Return>", createQR)
enter.place(x=5, y=5)

button = Button(zone2, text="Create", width=12, height=2, command= createQR)
button.place(x=12, y=35)

button2 = Button(zone2, text="Save", width=12, height=2, command= saveQR)
button2.place(x=130, y=35)

button3 = Button(zone2, text="Close", width=12, height=2, command= window.quit)
button3.place(x=260, y=35)

""" RUNNING """
window.mainloop()