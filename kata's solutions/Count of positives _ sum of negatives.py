# https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    count, result = 0, 0
    
    if len(arr) > 0:
        for i in arr:
            if i > 0:
                count += 1
            else:
                result += i
    else:
        return []

    return [count, result]