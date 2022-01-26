from operator import truediv
from wsgiref.handlers import IISCGIHandler


firstname = "Will"
lastname = "Spedding-Jones"
print ("hello" + " " + firstname + " " + lastname)

word1 = "Good "
word2 = "Day "
word3 = "Will"

sentence = word1 + word2 + word3
print(sentence)

number1 = input("13")
number2 = input("3.4")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(round_number)

name = "Woofingon"
age = 5
bark = True
tweet = False

books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"JR.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}

print(books["The Handmaiden's Tale"])

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)