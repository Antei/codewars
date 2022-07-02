# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a, b):
    return sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))

def get_sum2(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(1, 2))
print(get_sum(1, 7))
print(get_sum(0, 1))
print(get_sum(0, -1))