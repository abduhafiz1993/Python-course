name = input("What's your name? ")

with open("names.txt", "a") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
