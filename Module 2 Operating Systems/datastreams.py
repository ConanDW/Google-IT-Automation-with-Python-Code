noma = input("Was ist de noma: ")
print("Hallo, " + noma)

# env vars
import os 

print("Home: " + os.environ.get("Home", ""))
print("Shell: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))


#shell enviroment 


import sys 

print(sys.argv)