import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("Info", "Clicked Button")

root = tkinter.Tk()
root.title("Message Box")
root.geometry("400x200")
btn = tkinter.Button(text="Test", command=click_btn)
btn.pack()
root.mainloop()
