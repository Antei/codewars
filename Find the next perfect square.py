# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/

def find_next_square(sq):
    if int(sq ** 0.5) == float(sq ** 0.5):
        return ((sq ** 0.5) + 1) ** 2
    else:
        return -1


print(121 ** 0.5)
print(155 ** 0.5)