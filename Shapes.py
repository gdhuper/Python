import turtle 

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")

    t = turtle.Turtle()
    t.shape("turtle")
    t.color("orange")
    t.speed(50)
    
    
    for i in range(1,37):
        count = 0
        while(count < 4):
            t.forward(100)
            t.right(90)
            count = count + 1
        t.right(10)
     
    window.exitonclick()

draw_square()
