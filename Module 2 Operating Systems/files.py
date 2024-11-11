with open("spider.txt") as file:
    for line in file:
        print(line.upper())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())



file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)


with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")


with open("sample_data/declaration.txt", "rt") as textfile:
    for line in textfile:
        print(line)



f = open('workfile', 'w', encoding="utf-8")