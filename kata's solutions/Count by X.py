# https://www.codewars.com/kata/5513795bd3fafb56c200049e

def count_by(x, n):
    return [x * i for i in range(1, n + 1)]


print(count_by(2, 5))
print(count_by(1, 10))