user_funds = 10.31
item_price = int(input("Burger price: "))

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you don't have enough money")

def product(n):
    total = 1
    for i in n:
        total *= i
        return total
print(product((4,4,5)))  

#import pdb

#pdb.set_trace()

def is_prime(x):
    if x <= 2:
        return True
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            else:
                return True
print(is_prime(25))


#item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
#n = 0

#while n < 5:
#    for i in item_list:
#        print(i)
 #       n +-1
#print (item_list[n-1])
