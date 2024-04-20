"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    timmy = turtle.Turtle()
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    window = Tk()
    window.withdraw()
    day = simpledialog.askstring(title="Day", prompt="What day is it?")
    is_weekend = day == 'Saturday' or day == 'Sunday'
    if is_weekend:
        messagebox.showinfo(title="Weekend", message="Finally! I'm going back to sleep...")
    else:
        messagebox.showinfo(title="Weekday", message="That sucks.")
    score = simpledialog.askstring(title="Exam", prompt="Wait... did you pass your exam?")
    passed_exam = score == 'Yes'
    if passed_exam:
        messagebox.showinfo(title="Passed", message="Nice job!")
    else:
        messagebox.showinfo(title="Failed", message="You're a failure.")
    game = simpledialog.askstring(title="Game", prompt="Should the game be over?")
    game_over = game == 'Yes'
    if game_over:
        messagebox.showinfo(title="Game Over", message="The game is over.")
    else:
        messagebox.showinfo(title="Game... not Over?", message="The game will continue for eternity I guess...")
    rs = simpledialog.askstring(title="Crimson Cube", prompt="You should type 'red square'.")
    red = rs == 'red' or rs == 'red square'
    square = rs == 'square' or rs == 'red square'
    if red and square:
        messagebox.showinfo(title="Ready?", message="Nice!")
        timmy.pencolor("red")
        timmy.color("red")
        timmy.pendown()
        for i in range(400):
            timmy.forward(100)
            timmy.left(90)
    elif red:
        messagebox.showinfo(title="Red", message="Halfway there!")
        for i in range(400):
            timmy.pencolor("red")
            timmy.color("red")
            timmy.forward(i)
            timmy.left(i)
    elif square:
        messagebox.showinfo(title="Square", message="At least you know geometry.")
        for i in range(40):
            timmy.forward(100)
            timmy.left(90)
        for j in range(400):
            timmy.forward(100)
            timmy.left(90 - j)
    else:
        messagebox.showinfo(title="?", message="Ok..?")

    pass
