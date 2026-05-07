from utils import *

# Section 1 - setup
# TODO - set a background using set_background()

# TODO - create at least two variables and set their starting value. ex: cookies = 0
set_background("Shopping-Mall")

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()
m2 = create_sprite("balloon",-200,230)
m2.hideturtle()
m3 = create_sprite("rocket", -200, 170)
m3.hideturtle()
m4 = create_sprite("puppy", -200, 140)
m4.hideturtle()
money = 0
clothes = 0
food = 0
drink = 0

# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_money ():
    global money
    money += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    s1=create_sprite("Money",x,y)
    time.sleep(0.1)
    s1.hideturtle()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(get_money,"space")
# TODO - make a second control

def buy_clothes():
    global money, clothes
    if money >= 20:
        clothes += 1
        money -= 20
    
        x = random.randint(-200,200)
        y = -250
        create_sprite("shopping", x, y)
window.onkeypress(buy_clothes, "c")

def buy_food():
    global money, food
    if money >= 10:
        food += 1
        money -= 10
        x = random.randint(100,300)
        y = 200
        create_sprite("burger", x, y)
window.onkeypress(buy_food, "f")

def buy_drink():
    global money, drink
    if money >= 20:
        drink += 1
        money -= 20
        x = random.randint(100,300)
        y = 50
        create_sprite("Starbucks", x, y)
window.onkeypress(buy_drink, "d")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m2.clear()
    m3.clear()
    m4.clear()
    m1.color("pink")
    m1.write(f"Money is {money}",font = ("Arial", 20, "normal"))
    m3.color("pink")
    m3.write(f"Clothes is {clothes}",font = ("Arial", 20, "normal"))
    m2.color("pink")
    m2.write(f"Food is {food}",font = ("Arial", 20, "normal"))
    m4.color("pink")
    m4.write(f"Drink is {drink}",font = ("Arial", 20, "normal"))

    time.sleep(0.01)
    window.update()