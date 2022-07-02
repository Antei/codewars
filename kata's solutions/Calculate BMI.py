# https://www.codewars.com/kata/57a429e253ba3381850000fb

def bmi(weight, height):
    index = weight / height ** 2
    if index <= 18.5:
        return 'Underweight'
    elif index <= 25:
        return 'Normal'
    if index <= 30:
        return 'Overweight'
    else:
        return 'Obese'


# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"