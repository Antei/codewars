def make_negative(number):
    return number - (number * 2) if number > 0 else number


def make_negative2(number):
    return -abs(number)