# https://www.codewars.com/kata/568d0dd208ee69389d000016/

def rental_car_cost(d, cost=40):
    if d >= 7:
        return d * cost - 50
    if d >= 3:
        return d * cost - 20
    else:
        return d * cost