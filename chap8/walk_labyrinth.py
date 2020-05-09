import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

mx = 1
my = 1
def main_proc():
    global mx, my
    if key == "Up" and meiro[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and meiro[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and meiro[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and meiro[my][mx+1] == 0:
        mx = mx + 1
    canvas.coords("MYCHAR", mx*80+40, my*80+40)
    root.after(150, main_proc)

root = tkinter.Tk()
root.title("Walk labyrinth")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

meiro = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

for y in range(7):
    for x in range(10):
        if meiro[y][x] == 1:
            canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79, fill="skyblue", width=0)

img = tkinter.PhotoImage(file="images/mimi_s.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHAR")
main_proc()
root.mainloop()
