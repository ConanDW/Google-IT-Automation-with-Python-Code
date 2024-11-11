x = {}
type(x)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
#indexing dicts

file_counts["txt"]

"jpg" in file_counts
file_counts["cfg"] = 8
print(file_counts)
#deleting

del file_counts["cfg"]

for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("Ext: ", ext, " | " ,"Amounts: ", amount)

file_counts.keys()
 
file_counts.values()

for value in file_counts.values():
    print(value)

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result