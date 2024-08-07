import turtle

BODY_COLOR = 'RED'

BODY_SHADOW = ''

GLASS_SHADOW = ''

GLASS_COLOR = 'skyblue'

s = turtle.getscreen()
s.title("Among Us")
t = turtle.Turtle()


# WE WILL DIVIDE CHARACTER INTO 3 PARTS :

# BODY , GLASS, BACKPACK

# FIRST CREATE BODY()


def body():
    t.pensize(20)

    t.fillcolor(BODY_COLOR)

    t.begin_fill()

    # Right side

    t.right(90)

    t.forward(50)

    t.right(180)

    t.circle(40, -180)

    t.right(180)

    t.forward(200)

    # head curve

    t.right(180)

    t.circle(100, -180)

    # Left side

    t.backward(20)

    t.left(15)

    t.circle(500, -20)

    t.backward(20)

    # t.backward(200)

    t.circle(40, -180)

    t.left(7)

    t.backward(50)

    # hip

    t.up()

    t.left(90)

    t.forward(10)

    t.right(90)

    t.down()

    # t.right(180)

    # t.circle(25,-180)

    t.right(240)

    t.circle(50, -70)

    t.end_fill()


# NOW WE WILL CREATE GLASS() FUNCTION...

def glass():
    t.up()

    t.right(230)

    t.forward(100)

    t.left(90)

    t.forward(20)

    t.right(90)

    t.down()

    t.fillcolor(GLASS_COLOR)

    t.begin_fill()

    t.right(150)

    t.circle(90, -55)

    t.right(180)

    t.forward(1)

    t.right(180)

    t.circle(10, -65)

    t.right(180)

    t.forward(110)

    t.right(180)

    # t.right(180)

    t.circle(50, -190)

    t.right(170)

    t.forward(80)

    t.right(180)

    t.circle(45, -30)

    t.end_fill()


# NOW WE WILL CREATE BACKPACK() FUNCTION...

def backpack():
    t.up()

    t.right(60)

    t.forward(100)

    t.right(90)

    t.forward(75)

    t.fillcolor(BODY_COLOR)

    t.begin_fill()

    t.down()

    t.forward(30)

    t.right(255)

    t.circle(300, -30)

    t.right(260)

    t.forward(30)

    t.end_fill()


# NOW ITS TIME TO CALL OUR ALL FUNCTIONS ... SO LETS DO IT.

body()

glass()

backpack()

turtle.done()