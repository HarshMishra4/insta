import tkinter, random

window = tkinter.Tk()
window.geometry('300x300')

dice = tkinter.Label(window, font= ('Times', 200), foreground='red')

def roll_dice():
    pattern = [
        '\u2680',
        '\u2681',
        '\u2682',
        '\u2683',
        '\u2684',
        '\u2685',
    ]
    dice.config(text=random.choice(pattern))
    dice.pack()

button = tkinter.Button(window, text= 'Roll Dice', command= roll_dice)
button.place(x = 120, y =250)

roll_dice()
window.mainloop()
