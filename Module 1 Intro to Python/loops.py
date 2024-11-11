x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


while x % 2 == 0:
    x = x / 2 #loop that never ends


#better approach below

while x != 0 and x % 2 ==0:
    x = x / 2

multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

for x in range(5):
    print(x)


friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends: #should be foreach
    print("Hi " + friend)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " - Average: " + str(sum/length)) 


product = 1 
for n in range(1,10):
    product = product * n

print(str(product))

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + '|' + str(right) + "]", end="")
    print()

testVarRange = 10
while testVarRange < 20: 
    testVarRange += 1
    print(str(testVarRange))
    print("Space")
    print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams: 
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

greeting = "Hallo"
for char in greeting:
    if char == "a" or char == "l":
        print(char)
    else:
        print("Not a or L")

index = 0
while index < len(greeting):
    print(greeting[index])
    index += 1 

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)


string1 = "Greetings, Earthlings"

print(string1[0])
print(string1[1:11])

#example of stride,
print(string1[0::2])


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

