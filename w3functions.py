def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print (multiply((8, 2, 3, -1, 7)))

def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))

def even_numbers(numbers):
    even = []
    for x in numbers:
        if x % 2 == 0:
            even.append(x)
    return even
print(even_numbers((1, 2, 3, 4, 5, 6, 7, 8, 9)))  
   