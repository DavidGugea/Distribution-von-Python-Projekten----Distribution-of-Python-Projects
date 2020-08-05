import random

def randomNumbers(am):
    ls = list()
    if am < 1000:

        for i in range(am):
            ls.append(random.randint(1, 100))
    else:
        ls.append(1)

    return ls
