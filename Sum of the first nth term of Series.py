# https://www.codewars.com/kata/555eded1ad94b00403000071

def series_sum(n):
    if n == 1:
        return '1.00'
    if n == 0:
        return '0.00'
    result, delimiter = 1, 4
    for _ in range(n - 1):
        result += 1 / delimiter
        print(f'1/{delimiter}')
        delimiter += 3
    return '{:0.2f}'.format(result)


def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

print(series_sum(1))
print(series_sum(2))
print(series_sum(3))
print(series_sum(5))