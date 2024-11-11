from inspect import _void


def to_celsius(x):
    '''Convert Fahrenheit to Celsius'''
    return (x-32) * 5/9

test = to_celsius(75)
print(test)


number = -4 

if number > 0:
    print("Number is Positive")
elif number == 0:
    print("Number is zero.")
else:
    print("Number is negative.")


print(type(2.5))

testStr: str = "weird way to do types python"
area = 6*3/2
print("The area of the triangle is: " + str(area))


#fucntions


def greeting(name, department):
    print("Welcome, " + name)
    print("You are of " + department)

greeting("Cameron", "DevOps")

month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)
string_representation = str(7)
print(string_representation)

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)

print(min(time_list))
print(max(time_list))


def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(str(hours, minutes, seconds))

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Cameron")


#conditionals


print(2 > 1) #why not -gt
print("cat" == "dog")
print(1 != 2) #not equal or -ne 


#and, or, not
print(1 > 2 and 2 > 1)


print(25 > 50 or 1 != 2)

print(not 42 == "Answer")

print()


def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must not be longer than 15 characters long.")
    else:
        print("Valid username")


print("I miss my brackets and strong types")

