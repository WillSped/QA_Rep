#print("William Spedding-Jone\n139 Langbourne Place \nLondon \nE14 3WW")

#print(("Hello"), input("Please insert name: "))

#Length = float(input("Please insert the length in feet"))
#Width = float(input("Please insert the width in feet"))

#Area = (Length * Width)/43560

#print("the area is ", Area, "acres")

#small = int(input("Please insert number of smaller containers: "))
#big = int(input("Please insert number of larger containers: "))

#littlebottle = 0.10
#bigbottle = 0.25

#total = (small*littlebottle)+(big*bigbottle)
#print("Your refund total is $ ", total)

#meal = float(input("Please insert meal price: "))
#tip = 0.18
#tax = 0.20
#total = meal + (meal*tip) + (meal*tax)
#print("Your total meal cost is %.2f" % (total))

#n = int(input("Please select a number: "))
#sum = (n*(n+1))/2
#print("sum = ",sum)

#widgetw = 75
#gizmow = 112

#widgno = int(input("Please enter the number of widgets ordered: "))
#gizno = int(input("Please enter the number of gizmos ordered: "))

#total = (widgetw*widgno)+(gizmow*gizno)

#print("The total weight of your order is",total,"g")

#from cmath import log10
#import math
#a = int(input("Please choose a number for a: "))
#b = int(input("Please choose a number for b: "))

#sm = a+b
#dif = a-b
#prod = a*b
#quot = a/b
#rem = a%b
#lg = log10(a)
#pwr = a**b 

#inputcents = int(input("Please insert your number of cents: "))
#centsperpenny = 1
#centspernickel = 5
#centsperdime = 10
#centsperquarter = 25
#centsperloonie = 100
#centspertoonie = 200

#print(inputcents // centspertoonie, "toonies")
#inputcents = inputcents % centspertoonie

#inchcm = 2.54
#feetft = 12
#print("Please input your height: ")
#feet = int(input("Feet"))
#inch = int(input("Inches"))
#height = (feet*feetft + inch)*inchcm
#print("Your total height in cm is: ",height)

#mass = int(input("Please enter the mass of water: "))
#temp = int(input("Please enter the temperature change of water: "))
#cap = 4.186
#eng = mass*cap*temp
#print("The total energy change is ", eng)


#from cmath import sqrt


#acc = 9.8
#vinit = 0
#height = int(input("Please insert height in meters: "))

#vfinal = sqrt(2*acc*height)
#print("The final speed of object is",vfinal,"meters per second^2")

#numb = int(input("Please select an integer"))
#if numb % 2 == 0:
#    print("Your number is even")
#else:
#         print("Your number is odd")

#letter = str(input("Please choose a letter of the alphabet" ))
#vwl = ["a", "e", "i", "o", "u"]
#if letter in vwl:
#    print ("Your letter is a vowel")
#elif letter == "y":
#    print ("Sometimes y is a vowel, sometimes a consanant")
#else:
#    print ("Your letter is a consanant")

#Month = input("Please select a month of the year")
#if Month == "february":
#    print("28 or 29 days")
#elif Month in ["April", "June", "September", "November"]:
#    print("30 days")
#else:
#    print("31 days")

#length1 = int(input("Please insert length 1: "))
#length2 = int(input("Please insert length 2: "))
#length3 = int(input("Please insert length 3: "))

#if length1 == length2 and length2 == length3 and length1 == length3:
#    print("equilateral triangle")
#elif length1 == length2 or length2 == length3 or length1 == length3:
#    print("iscosceles triangle")
#else:
#    print("scalene triangle")

#month = input("Please select a month: ")
#day = input("Please select a day: ")

#if month == "january" and day == "1":
#        print("New Year's Day")
#elif month == "july" and day == "1":
#        print("Canada Day")
#elif month == "december" and day == "25":
#        print("Christmas Day HOHOHO")
#else:
#    print("No holiday :'(")  
#

#month = input("Please select a month: ")
#day = input("Please select a day: ")

#if month == "january" or month == "february":
#    season = "winter"
#elif month == "march":
#    if day > 20:
#        season = "winter"
#    else:
#        season = "spring"

from itertools import count


#total = 0.00
#inc = 0
#avg = (input("Please select a number, entering 0 after the final number"))
#while avg != "0":
#    total = total + int(avg)
#    avg = (input("Please select a number, entering 0 after the final number"))
#    inc += 1 
#average = total / inc
#print("The average of your numbers is",average)
    
#penniespernickel = 5
#nickel = 0.05

#total = 0.00
#price = (input("Please enter a price: "))
#while price != "":
#    total = total + float(price)
#    price = (input("Please enter a price: "))

#print("The amount payable is:",total)

#babyprice = 0.00
#childprice = 14.00
#adultprice = 23.00
#seniorprice = 18.00

#babylimit = 2
#childlimit = 12
#adultlimit = 64

#total = 0
#agecost = input("Please enter the guest's age: ")
#while agecost != "":
#    age = int(agecost)
#    if age <= babylimit:
#        total = total + babyprice
#    elif age <= childlimit:
#        total = total + childprice
#    elif age <= adultlimit:
#        total = total + adultprice
#    else:
#        total = total + seniorprice
#    agecost = input("Please enter the guest's age: ")

#print ("The total price for the group is: ",total)

#line = input("Enter 8 bits: ")

#while line != "":
#    if line.count("0") + line.count("1") != 8 or len(line) != 8:
#        print("You did it wrong you numpty, enter again: ")
#    else:
#        ones = line.count("1")
#        if ones % 2 == 0:
#            print("The parity bit should be 0.")
#        else:
#            print ("The parity bit should be 1.")
#    line = input("Enter 8 bits: ")        


        



