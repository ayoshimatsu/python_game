import tkinter

def click_btn():
    text.insert(tkinter.END, "Appear something!")

root = tkinter.Tk()
root.title("Multiple lines")
root.geometry("400x200")
button = tkinter.Button(text="Message", command=click_btn)
button.pack()
text = tkinter.Text()
text.pack()
root.mainloop()