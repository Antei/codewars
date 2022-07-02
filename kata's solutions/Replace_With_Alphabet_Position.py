# https://www.codewars.com/kata/546f922b54af40e1e90001da/

def alphabet_position(text):
    return ' '.join(str(ord(i) - ord('a') + 1) for i in text.replace(' ', '').lower() if i.isalpha())

def alphabet_position2(text):
    return ' '.join(str(ord(i) - 96) for i in text.lower() if i.isalpha())