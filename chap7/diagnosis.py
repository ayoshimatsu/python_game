import tkinter

RESULT = [
    "There is no possibility that your past lif was cat",
    "Normal people",
    "There is nothing special",
    "There is something like cat",
    "Your character is like cat",
    "Your character is very like cat",
    "Your previous life might be cat",
    "You are cat"
]

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    nekodo = int(100*pts/7)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "Rate of cat is " + str(nekodo) + " %.\n" + RESULT[pts])


root = tkinter.Tk()
root.title("Diagnosis App")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="images/sumire.png")
canvas.create_image(400, 300, image=gazou)

button = tkinter.Button(text="Diagnosis", font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)

text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

bvar = [None] * 7
cbtn = [None] * 7
ITEM = [
    "Like high place",
    "Feel like rolling ball when look at it",
    "Hair rise when get surprised",
    "Curious about toy of mouse",
    "Sensitive to smell",
    "Feel like picking fish bone",
    "Get energetic at night"
]

for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160+40*i)


root.mainloop()