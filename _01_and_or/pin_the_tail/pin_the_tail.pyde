"""
The player of the game has to click the mouse where the donkey's
tail will go. The problem is, the picture keeps disappearing!
"""

def setup():
    size(800, 600)
    
    global donkey
    donkey = loadImage('donkey.jpg')
    donkey.resize(width, height)
    
    global tail
    tail = loadImage('tail.png')
    
    global x
    global y
    x = None
    y = None
    global stuck
    stuck = 0
    noStroke()
    
def draw():
    global x
    global y
    global stuck
    # 1. Use the background() function to draw the donkey
    if(mouseX > 0 and mouseX < 30 and mouseY > 0 and mouseY < 30):
        background(donkey)
    else:
        background(0, 0, 0)
    # 2. Use the rect() function to draw a box in the upper left
    # corner of the screen:
    # rect(0, 0, 30, 30)
    rect(0, 0, 30, 30)
    # 3. Now find the x and y coordinates where the tail attaches
    # to the donkey and draw another box with a side of 50

    # 4. Change your code so the donkey is only shown when the
    # mouse is inside the corner bounding box. 
    #
    # Hint: check if mouseX is greater than 0 and less than 30
    # and y is greater than 0 and less than 30
    
    # 5. Check that when the mouse is outside the corner box,
    # you should show a solid color background.
    if mousePressed:
        stuck = 1
        x = mouseX
        y = mouseY
    # 6. Use the image() method to draw the tail at the mouseX
    # and mouseY location. For example,
    # image(tail, mouseX, mouseY)
    if stuck == 1:
        image(tail, x, y)
        if(x > 695 and x < 745 and y > 169 and y < 219):
            print("You win!")
            background(donkey)
            image(tail, x, y)
        else:
            print("You lose!")
            background(donkey)
            image(tail, x, y)
    else:
        image(tail, mouseX, mouseY)
    # 7. Now, adjust your code so the tail sticks when you click the
    # mouse (this means it will no longer move when the mouse moves)
    #
    # Hint: you will need to use the mousePressed variable and set the
    # x and y variables declared in setup()

    # 8. When the tail has been pinned, write code to check if the
    # tail was pinned inside the target bounding box.
    
    # 9. Show the donkey so the user knows where they pinned the tail.
    
