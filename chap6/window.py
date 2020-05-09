import tkinter
import random
from PIL import Image, ImageTk

def click_btn():
    label["text"] = random.choice(["Lucky", "Normal", "Take care", "Bad"])
    label.update()
    #button["text"] = "Button was clicked."

root = tkinter.Tk()
root.title("Test window")
#root.geometry("800x600")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=800, height=800, bg="skyblue")
canvas.pack()

#img = Image.open("../images/eyeGhost.jpeg")
img = Image.open(open('../images/eyeGhost.jpeg', 'rb'))
img_resize = img.resize((800, 800))
img_resize = ImageTk.PhotoImage(img_resize)
canvas.create_image(0, 0, image=img_resize, anchor=tkinter.NW)

#print(type(img))
#print(type(img_resize))

label = tkinter.Label(root, text="???", font=("System", 100), bg="green")
label.place(x=0, y=0)

button = tkinter.Button(root, text="Fortune", font=("Times New Roman", 50), fg="skyblue", command=click_btn)
button.place(x=0, y=600)

root.mainloop()
