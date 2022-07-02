# https://www.codewars.com/kata/5552101f47fc5178b1000050/

def dig_pow(n, p):
    sum_n = 0
    for num in str(n):
        sum_n += int(num) ** p
        p += 1
    k = sum_n / n
    if k == int(k):
        return int(k)
    return -1


print(dig_pow(89, 1)) # 1
print(dig_pow(92, 1)) # -1
print(dig_pow(46288, 3)) # 51