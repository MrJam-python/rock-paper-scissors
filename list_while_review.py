'''
Create a list with five of your favorite foods. From there, print out every single
thing in the list line by line

ex. input: Sushi, Burgers, Fries

output:
Sushi
Burgers
Fries

challenge problem:

a. Try printing out the list backwards
b. Try printing out the list in this format:

1. Sushi
2. Burgers
3. Fries
'''
fav_foods = ["Pizza", "Alfredo", "Lasagna"]
selected_food_num = 0

while selected_food_num <= 2:
    print (fav_foods[selected_food_num])
    selected_food_num += 1

# integers: 1, 2, 100, 1000, -1, etc.
selected_food_num = 0
while selected_food_num <= 2:
    print (str(selected_food_num + 1) + ". " + fav_foods[selected_food_num])
    selected_food_num += 1

selected_food_num =2

while selected_food_num >= 0:
    print (str(selected_food_num + 1) + ". " + fav_foods[selected_food_num])
    selected_food_num -= 1
