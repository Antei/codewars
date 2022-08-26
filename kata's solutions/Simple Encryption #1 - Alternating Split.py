# https://www.codewars.com/kata/57814d79a56c88e3e0000786/

# solve with hint

def decrypt(enc_text: str, n):
    if enc_text:
        i = len(enc_text) // 2

        for _ in range(n):
            a = enc_text[:i]
            b = enc_text[i:]
            enc_text = ''.join(b[i:i+1] + a[i:i+1] for i in range(i + 1))
        return enc_text
    return enc_text


def encrypt(text: str, n):
    for _ in range(n):
        text = ''.join(text[1::2]) + ''.join(text[0::2])
    return text