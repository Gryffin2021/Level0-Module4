"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    window = Tk()
    window.withdraw()
    score_1 = simpledialog.askinteger(title="Score on First Test", prompt="What was your score on the first test?")
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    score_2 = simpledialog.askinteger(title="Score on Second Test", prompt="What was your score on the second test?")
    # TODO) Take the average score of both tests (total score / 2)
    total_score = score_1 + score_2
    average_score = total_score/2
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    if average_score >= 89.5:
        messagebox.showinfo(title=None, message="A")
        messagebox.showinfo(title=None, message="Wow! You must have studied really hard for those tests!")
    elif average_score >= 79.5:
        messagebox.showinfo(title=None, message="B")
        messagebox.showinfo(title=None, message="Nice job! That's pretty good!")
    elif average_score >= 69.5:
        messagebox.showinfo(title=None, message="C")
        messagebox.showinfo(title=None, message="About average.")
    elif average_score >= 59.5:
        messagebox.showinfo(title=None, message="D")
        messagebox.showinfo(title=None, message="D is for 'you're a little on the dumber side'.")
    elif average_score < 59.5:
        messagebox.showinfo(title=None, message="F")
        messagebox.showinfo(title=None, message="You're going nowhere in life.")
    pass
