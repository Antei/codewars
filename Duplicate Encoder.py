# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word: str):
    text, result = word.lower(), ''

    for char in text:
        if text.count(char) > 1:
            result += ')'
        else:
            result += '('
    return result


def duplicate_encode(word: str):
    return "".join("(" if word.lower().count(c) == 1 else ")" for c in word.lower())


print(duplicate_encode("din") == "(((")
print(duplicate_encode("recede") == "()()()")
print(duplicate_encode("((((()") == ")))))(")
print(duplicate_encode("(( @") == "))((")
print(duplicate_encode("@G)WJtGLqQuty!y(w!hnf!RYnuoq C") == "()()())()))))))())()()()))()((")