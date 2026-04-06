from utils import *
# Section 1 - Variables
x1 = -300
y1 = 200
x2 = -300
y2 = 25
x3 = -300
y3 = -120
x4 = -300
y4 = -200


# Section 2 - Setup
set_background("hawaii")
t1 = create_sprite("character1",x1,y1)
t2 = create_sprite("fox",x2,y2)
t3 = create_sprite("turtle3",x3,y3)
t4 = create_sprite("alien",x4,y4)

time.sleep(3)
# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(35):
    x1 += 10
    x2 += 13
    x3 += 7
    x4 += random.randint(10,25)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
s5 = create_sprite ("lebron(1)",-90 -150)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!",font = ("Arial", 30, "normal"))
elif x2 >= x1 and x2 >= x3 and x2>= x4:
    s5.write("player 2 wins!",font = ("Arial", 30, "normal"))
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    s5.write("player 3 wins!",font = ("Arial", 30, "normal"))
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    s5.write("player 4 wins!",font = ("Arial", 30, "normal"))
turtle.exitonclick()