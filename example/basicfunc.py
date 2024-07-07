# function with no params
def hello():
    print("Hello, My name is Beagle")
    
hello()

# function with parameter
def hello_friend(name):
    print(f"Hello, my friend is {name}")

hello_friend("Jo")

# function with 2 parameters, string and integer
def checkNameAge(name, age):
    print(f"Name is {name}")
    print(f"{name} is {age} yrs")

checkNameAge("Josh", 25)
checkNameAge(25, "Josh")
checkNameAge(age=25, name="Josh")

# function with default argument
def is_okay(name, logic=True):
    if (logic == True):
        print(f"{name} is Okay")
    else:
        print(f"{name} is not okay")

is_okay("Bee",False)

# function with return value
def add_number(x, y):
	return x+y

sum = add_number(10, 30)
print("Summation of 10 and 30 is",sum)

# function to find leap year, the year with 366 days
# Divisible by 4 or not divisible by 100
# Divisible by 400

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} It's a leap year!!!")
    else:
        print(f"{year} It's not a leap year")

# year = int(input("Year : "))
# is_leap_year(year)

# Data struct list
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange']

# access colors list member
print(f"Colors number 2 is: {colors[2]}\n")

# add new element to the list
colors.append("gray")
colors.append("black")

# Iterate over colors list
print("Color is colors are :")
for color in colors:
    print(color.capitalize())
    # print(color.upper())
