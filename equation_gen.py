from random import * 

def quation_gen():
    list1 = ["-", "+"]
    list2 = ["x", "a", "n", "t", "i"]
    letter = choice(list2)
    s = choice(list1)
    f = randint(0, 1000)
    a = randint(1, 1000)
    b = randint(1, 1000)
    c = randint(1, 1000)
    quation = str(a) + letter + "^2 " + s + " " + str(b) + letter + " " + s + " " + str(c) + " = " + str(f)
    return quation
