import tkinter
FNT = ("Times New Roman", 30)

class GameCharacter:
    def __init__(self, aJob, aLife, aImgfile):
        self.job = aJob
        self.life = aLife
        self.img = tkinter.PhotoImage(file=aImgfile)

    def draw(self, x, y):
        canvas.create_image(x+200, y+280, image=self.img)
        canvas.create_text(x+300, y+400, text=self.job, font=FNT, fill="red")
        canvas.create_text(x+300, y+480, text=self.life, font=FNT, fill="blue")

root = tkinter.Tk()
root.title("object")
canvas = tkinter.Canvas(root, width=800, height=560, bg="white")
canvas.pack()

character = [
    GameCharacter("Warrior", 200, "image/swordsman.png"),
    GameCharacter("Ninja", 160, "image/ninja.png")
]

character[0].draw(0, 0)
character[1].draw(400, 0)

root.mainloop()