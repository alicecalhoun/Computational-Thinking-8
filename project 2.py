input("What animal are you?...click enter to do the quiz...")
dog_points = 0
horse_points = 0
seahorse_points = 0
fox_points = 0
cat_points = 0
spider_points = 0
answer1 = input("What would you do on a Saturday? A) lay on the couch, B) go into the forest C) go swimming, D) lay in the sun, E) run around your house:   ")
if answer1 == "A" or answer1 == "a":
    dog_points += 1
elif answer1 == "B" or answer1 == "b":
    horse_points += 1
elif answer1 == "C" or answer1 == "c":
    seahorse_points += 1
elif answer1 == "D" or answer1 == "d":
    fox_points += 1
elif answer1 == "E" or answer1 == "e":
    spider_points += 1
print("")
answer2 = input("What's your favorite weather? A) perfect temp and clear skies, B) A little cold, C) sunny, D) snowy, E) rainy:   ")
if answer2 == "A" or answer2 == "a":
    dog_points += 1
elif answer2 == "B" or answer2 == "b":
    horse_points += 1
elif answer2 == "C" or answer2 == "c":
    seahorse_points += 1
elif answer2 == "D" or answer2 == "d":
    fox_points += 1
elif answer2 == "E" or answer2 == "e":
    spider_points += 1
print("")
answer3 = input("If you could have any super power would it be...? A) Being able to run as far w/ out getting tired B) Super high jumping C) breathing underwater D)invisibility E)walking on walls:   ")
if answer3 == "A" or answer3 == "a":
    dog_points += 1
elif answer3 == "B" or answer3 == "b":
    horse_points += 1
elif answer3 == "C" or answer3 == "c":
    seahorse_points += 1
elif answer3 == "D" or answer3 == "d":
    fox_points += 1
elif answer3 == "E" or answer3 == "e":
    spider_points += 1
print("")
answer4 = input("What food do you like to eat? A) Chicken B) Carrots or Apples C) Seafood D) Meat E) crickets:   ")
if answer4 == "A" or answer4 == "a":
    dog_points += 1
elif answer4 == "B" or answer4 == "b":
    horse_points += 1
elif answer4 == "C" or answer4 == "c":
    seahorse_points += 1
elif answer4 == "D" or answer4 == "d":
    fox_points += 1
elif answer4 == "E" or answer4 == "e":
    spider_points += 1
print("")
answer5 = input("What's your favorite hobby? A) Sleeping B) Running C) Swimming D) Hiking E) Climbing:    ")
if answer5 == "A" or answer5 == "a":
    dog_points += 1
elif answer5 == "B" or answer5 == "b":
    horse_points += 1
elif answer5 == "C" or answer5 == "c":
    seahorse_points += 1
elif answer5 == "D" or answer5 == "d":
    fox_points += 1
elif answer5 == "E" or answer5 == "e":
    spider_points += 1
print("~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")
if dog_points > horse_points and dog_points > seahorse_points and dog_points > fox_points and dog_points > spider_points:
    print("Your animal is a Dog!!!")
elif horse_points > dog_points and horse_points > seahorse_points and horse_points > fox_points and horse_points > spider_points:
    print("Your animal is a Horse!!!")
elif seahorse_points > dog_points and seahorse_points > horse_points and seahorse_points > fox_points and seahorse_points > spider_points:
    print("Your animal is a Seahorse!!!")
elif fox_points > dog_points and fox_points > horse_points and fox_points > seahorse_points and fox_points > spider_points:
    print("Your animal is a Fox!!!")
elif spider_points > dog_points and spider_points > horse_points and spider_points > seahorse_points and spider_points > fox_points:
    print("Your animal is a Spider!!!")
print("~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")