def off(c):
    if c.isalpha():
        return (ord(c) - ord('A') if c.isupper() else ord(c) - ord('a'))
    else:
        return None

def shift(i, n):
    return 0 if i is None else ((i + n + 26) % 26 - i)

def rot(s, n):
    return "".join(chr(ord(c) + shift(off(c), n)) for c in s)

def secret():   
    v = raw_input("Enter your message: ")
    k = int(raw_input("Enter a number: "))
    print rot(v, k)

secret()

