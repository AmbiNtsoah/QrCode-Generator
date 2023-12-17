from tkinter import *
import qrcode

""" INITIALIZATION """
window = Tk()
window.title("QrCode Generator")
window.config(bg="gray")
window.geometry("800x500")
window.resizable(0,0)
icon = PhotoImage(file="images/unnamed.png")
window.iconphoto(False,icon)


""" CONTENT """



textEnter = Label(window, text="Enter your text bellow", font=('Arial', 12))
textEnter.pack(pady=14)
textZone = Text(window, height=1, width=30, font=('Arial',12))
textZone.pack()
validate = Entry(window, width=30)
validate.pack(pady=10)
generating = Button(window, width=15, height=2, text="Generate")
generating.pack()


""" RUNNING """
window.mainloop()