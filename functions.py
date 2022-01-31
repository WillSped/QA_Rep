from typing import ClassVar


def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number + 20)


def scores(modules):
    total = 1
    for x in modules:
        total = (homework + assesment + exam) / 175 * 100
    return total
name = str(input("Please insert your name: "))    
homework = int(input("Please input homework mark: "))
assesment = int(input("Please input assessment mark: "))
exam = int(input("Please input exam score: "))
print(scores(name))



