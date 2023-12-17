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
def createQR(*args):
    ...




def saveQR(*args):
    ...






zone1 = Frame(window, bd=2, relief=RAISED)
zone1.place(x=10, y=5, width=380, height=390)

zone2 = Frame(window, bd=2, relief=SUNKEN)
zone2.place(x=10, y=405, width=380, height=80)

enter = Entry(zone2, width=40, font=("Robotto", 12), justify=CENTER)
enter.place(x=5, y=5)

button = Button(zone2, text="Create", width=15, height=2, command= createQR)
button.place(x=12, y=35)

button2 = Button(zone2, text="Save", width=15, height=2, command= saveQR)
button2.place(x=130, y=35)

button3 = Button(zone2, text="Close", width=15, height=2, command= window.quit)
button3.place(x=250, y=35)

""" RUNNING """
window.mainloop()