import turtle
import time

# create a screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("#b3daff")
# set tile of screen
screen.title("The National Flag, Tiranga")
drawn = turtle.Turtle()
# set the cursor/turtle speed. Higher value, faster is the turtle
drawn.speed(3)
drawn.penup()
# decide the shape of cursor/turtle
drawn.shape("triangle")


# flag height to width ratio is 2:3
flag_height = 300
flag_width = 450

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -225
start_y = 150

# For saffron, white and green stripes. each strip width will be flag_height/3 = 100
stripe_height = flag_height/3
stripe_width = flag_width

# Radius of Ashok Chakra, half of white stripe 
chakra_radius = stripe_height / 2


def draw_fill_rectangle(x, y, height, width, color):
    drawn.goto(x,y)
    drawn.pendown()
    drawn.color(color)
    drawn.begin_fill()
    drawn.forward(width)
    drawn.right(90)
    drawn.forward(height)
    drawn.right(90)
    drawn.forward(width)
    drawn.right(90)
    drawn.forward(height)
    drawn.right(90)
    drawn.end_fill()
    drawn.penup()


# this function is used to create 3 stripes
def draw_stripes():
    x = start_x
    y = start_y
    # we need to draw total 3 stripes, 1 saffron, 1 white and 1 green
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#FF9933")
    # decrease value of y by stripe_height
    y = y - stripe_height   
    # create middle white stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height               

    # create last green stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#138808')
    y = y - stripe_height


def draw_chakra():
    drawn.speed(1)
    drawn.goto(0,0)
    color = "#000080" # navy blue
    drawn.penup()
    drawn.color(color)
    drawn.fillcolor(color)
    drawn.goto(0, 0 - chakra_radius)
    drawn.pendown()
    drawn.circle(chakra_radius)
    # draw 24 spikes in chakra
    for _ in range(24):
        drawn.penup()
        drawn.goto(0,0)
        drawn.left(15)
        drawn.pendown()
        drawn.forward(chakra_radius)
  
    

time.sleep(0)
draw_stripes()
draw_chakra()
drawn.hideturtle()
screen.mainloop()
