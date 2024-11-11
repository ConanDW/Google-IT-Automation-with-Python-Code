#READD OTHER STRING THINGS FROM STUFF YOU NEED TO SEND FROM HOME


"Moutains".upper()
"Moutains".lower()




answer = "YES"

if answer.lower() == "YES":
  print(answer.strip(" "))


" yes ".rstrip()
" yes ".lstrip()

"Forest".endswith("rest")
"Forest".isnumeric() #tests if a string of numbers or not 
int("12345") + int("54321") # makes inits
" ".join(['Pwsh', 'Over', 'Py'])
"test of slipt".split()

name = "Manny"
number = len(name) * 3
print("Hello {}, you lucky number is {}".format(name, number))
#if it gets more complex you can do this:

print("Your lucky number is {number}, {name}.".format(name = name, number = len(name)*3))
#formating expressions:
price = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

