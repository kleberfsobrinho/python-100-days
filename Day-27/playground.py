# Unlimited Arguments
def add(*args):
    numbers_sum = 0
    for n in args:
        numbers_sum += n
    return numbers_sum


print(add(3, 5, 6))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)
