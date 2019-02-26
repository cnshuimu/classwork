# Q34
try:
    num = int(input("enter a number: "))
except ValueError:
    print('Value must be an integer')
else:
    if num % 2 == 0:
        print("it is an even number")
    elif num % 2 == 1:
        print("it is an odd number")

# Q35
human_year = float(input("enter a human year: "))
if human_year <= 2 and human_year >= 0:
    dog_year = human_year * 10.5
    print(dog_year)
elif human_year > 2:
    dog_year = 13 + 4 * human_year
    print(dog_year)
else:
    print("do not enter a neagtive number")

# Q36
vowel = ["a", "e", "i", "o", "u"]
letter = input("please enter a letter: ")
if letter in vowel:
    print("it a a vowel")
elif letter == "y":
    print("sometimes it is a vowel, sometimes it is a consonant")
else:
    print("it is a consonant")

#  Q37
shape = ["triangle","quadrilateral","pentagon","hexagon","heptagon","octagon","nonagon","decagon"]
sides = int(input("please enter the number of sides: "))
index = sides - 3
if sides >= 3 and sides <= 10:
    print(shape[index])
else:
    print("the sides are so many/few")

# Q48
zodiac = ["dragon","snake","horse","sheep","monkey","rooster","dog","pig","rat","ox","tiger","hare"]
year = int(input("enter a year: "))
index = (year + 4) % 12
if year >= 0:
    print(year, "is the year of", zodiac[index] )
else:
    print("do not enter a negative year number")
