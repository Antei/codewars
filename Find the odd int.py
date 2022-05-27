# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq: list):
    return [i for i in seq if seq.count(i) % 2 != 0][0]


# через оператор:
# https://www.codewars.com/kata/reviews/56257b3f27e918efed00017c/groups/562b4088d9377354db000032