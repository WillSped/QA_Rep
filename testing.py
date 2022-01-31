def scores(modules):
    modules(Var1, Var2, Var3)
    for x in modules:
        total = (homework + assesment + exam) / 175 * 100
    return total
name = str(input("Please insert your name: "))    
homework = int(input("Please input homework mark: "))
assesment = int(input("Please input assessment mark: "))
exam = int(input("Please input exam score: "))
print(scores(name))