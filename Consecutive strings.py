# https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(strarr, k):
    result = ''
    if 0 <= k <= len(strarr):
        for i in range(len(strarr)):
            word = ''.join(strarr[i:i + k])
            if len(word) > len(result):
                result = word

    return result