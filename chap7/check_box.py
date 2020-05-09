import tkinter

def check():
    if cval.get() == True:
        print("Checked")
    else:
        print("Not checked")

root = tkinter.Tk()
root.title("Check button")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(False)
cbtn = tkinter.Checkbutton(text="check button", variable=cval, command=check)
cbtn.pack()
root.mainloop()