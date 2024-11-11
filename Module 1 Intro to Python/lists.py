x = ["Now", "we", "are", "cooking"]
type(x)
print(x)

"are" in x 

x[1:3]
x[:2]
x[2:]

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Cameron")
print(fruits)
fruits.insert(0, "Orange") #use insert for the beginning and append to the end
fruits.remove("Melon")
print(fruits)
fruits.pop(3)


#below is tuple same as list but immutable
fullname = ('Grace', 'M', 'Hopper')


#iterating over touples and lists 

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result

print(full_emails([("alex@ex.com", "Alex Diego"), ("shay@ex.com", "Shay Bran")]))


multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

#same as above but list comprehnsion

multiples = [ x*7 for x in range(1,11) ]

languages = ["python", "perl", "ruby", "go", "java", "dart", "c"]
lengths = [len(language) for language in languages]
print(lengths)
#you can also use conditionals in list comprehnsions

z = [x for x in range(0,101) if x % 3 == 0]

def odd_numbers(n):
	return [x for x in range(n + 1) if x  % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
#REMEBER THAT RANGE STARTS AT ZERO AND END AT -1
#ALSO REMEBER THAT LISTS CAN CHANGE, TOUPLES CANNOT
# USE LIST COMPREHENSIONS FOR SIMPLE CODE AND FOR LOOPS FOR COMPLEX CODE.

