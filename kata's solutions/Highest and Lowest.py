# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return f'{max(nums)} {min(nums)}'