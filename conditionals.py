Mark = int(input("Please input a score: "))

if Mark > 85:
    print("Distinction")
elif Mark > 65:
    print ("Pass")
else:
    print("Fail")


Number = int(input("Please choose a number: "))
if Number % 2 == 0:
    print ("Your number is even!")
else:
    print ("Your number is odd!")     

Letter = (input("Please choose a letter of the alphabet: "))
if Letter == ["a", "e", "i", "o", "u"]:
    print ("Your letter is a vowel!")
elif Letter == "y":
    print ("Sometimes y is a vowel, sometimes it is a consonant")
else:
    print ("Your Letter is a consonant")

Shape = int(input("Please select a number of sides: "))    
if Shape == 3:
    print ("Your shape is a triangle")
elif Shape == 4:
    print ("Your shape is a square")
elif Shape == 5:
    print ("Your shape is a pentagon")
elif Shape == 6:
    print ("Your shape is a hexagon")
elif Shape == 7:
    print ("Your shape is a heptagon")
elif Shape == 8:
    print ("Your shape is an octogan")
elif Shape == 9:
    print ("Your shape is a nonagon")
elif Shape == 10:
    print ("Your shape is a decagon")
else:
    print ("Your number is out of this range, try again")

Year = int(input("Please choose a year to check: "))
if Year % 400 == 0:
    print ("Your number is a leapyear!")
elif Year % 100 == 0:
    print ("Your number is not a leapyear")
elif Year % 4 == 0: 
    print ("Your number is a leapyear!")
else:
    print ("Your number is not a leapyear")