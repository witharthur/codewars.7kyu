# Odd March Bits 8 bits
def bit_march (n : int) -> list:
    return [[0] * (8 - n - i) + [1] * n + [0] * i for i in range(8 - n + 1)]

# Quarter of the year
def greet(name):
    return "Hello, " + name + " how are you doing today?"

# Calculate average
def find_average(x):
    return sum(x)/len(x) 

# Calculate BMI
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"

# Fake Binary 
def fake_bin(x):    
    return ''.join('0' if c < '5' else '1' for c in x)

# Remove exclamation marks
def remove_exclamation_marks(s):
    return s.replace("!", "")

# Thinkful - Logic Drills: Traffic light
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"

# If you can't sleep, just count sheep!!
def count_sheep(n):
    sheep = ''
    for i in range(n):
        sheep+=f"{i+1} sheep..."
    return sheep

# Grasshopper - Summation
def summation(num):
    return num * (num + 1) / 2

# Will you make it?     
def zero_fuel(distance_to_pump, mpg, fuel_left):
        return mpg*fuel_left >= distance_to_pump

# Invert values
def invert(lst):
    return [n* -1 for n in lst] if len(lst)> 0  else []

# The Feast of Many Beasts
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# Function 3 - multiplying two numbers
def twoNumbers(a,b):
    return a*b

# Grasshopper - Personalized Message
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

# Volume of a Cuboid
def getVolumeOfCubiod(length, width, height):
    return length * width * height

# Is this a triangle?
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
