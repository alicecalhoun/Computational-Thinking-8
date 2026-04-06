input("What animal are you?...click enter to do the quiz...")
dog_points = 0
horse_points = 0
seahorse_points = 0
fox_points = 0
cat_points = 0
spider_points = 0
answer1 = input("What would you do on a Saturday? A) lay on the couch, B) go swimming, C) go in the forest, D) lay in the sun, E) run around your house: ")
if answer1 == "A":
    dog_points += 1
elif answer1 == "B":
    horse_points += 1
elif answer1 == "C":
    seahorse_points += 1
elif answer1 == "D":
    fox_points += 1
elif answer1 == "E":
    spider_points += 1
print("")
answer2 = input("What's your favorite weather? A) perfect temp and clear skies, B) A little cold, C) sunny, D) snowy, E) rainy: ")
if answer2 == "A":
    dog_points += 1
elif answer2 == "B":
    horse_points += 1
elif answer2 == "C":
    seahorse_points += 1
elif answer2 == "D":
    fox_points += 1
elif answer2 == "E":
    spider_points += 1
print("")
answer3 = input("")