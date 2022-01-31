class Category:

    
    def __init__(self,balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdrawl(self, amount):
        self.balance = self.balance - amount

    def transfer(self,amount,fromcatagory):
        fromcatagory.withdrawl(amount)
        self.balance = self.balance + amount

food = Category(0)
clothes = Category(15)
entertainment = Category(12)

print('#Food Account')
print(food.balance)
food.deposit(15)
print(food.balance)

food.transfer(15, clothes)

print(food.balance)


#food.transfer()

print(clothes.balance)
clothes.deposit(60)
print(clothes.balance)
clothes.withdrawl(12)
print(clothes.balance)