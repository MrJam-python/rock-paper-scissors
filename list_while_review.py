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


'''
Create a function called total_sum that takes a list of numbers and adds all of their values together. Test this function out with this list:

[1,2,3,4,5]

The answer you should get back is 15

ex. total_sum([1,2,3]) => 6, since 1 + 2 + 3 = 6
'''

# parameters => empty variables that represent data
def total_sum(numbers):
    sum = 0
    for x in numbers:
        sum += x
    print (sum)


# arguments => the data that you give the parameters so that they can be equal to something

total_sum ([])
total_sum ([56,8,32])
total_sum ([6,80,32])
total_sum ([56,80,3])



# create a function called calculator that takes in two numbers, and an operator (+, -, /, or *)
'''
This function will then multiply, divide, add, or subtract the two numbers and give back the answer depending on what operator they use

ex. calculator(5,2,'-') => 3
    calculator(3,30, '*') => 90
    calculator(10,3, '+') => 13
    

'''

def calculate(number1, number2, operator):
    if operator == "+":
        print (number1 + number2)
    
    if operator == "-":
        print (number1 - number2)
    
    if operator == "*":
        print (number1 * number2)
        
    if operator == "/":
        print (number1 / number2)

calculate(1,5,"/")


def greeting(name="anon"):
    print("Hello " + name)

greeting("James ")
greeting()
