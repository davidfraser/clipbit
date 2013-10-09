def off(c):
    if c.isalpha():
        return (ord(c) - ord('A') if c.isupper() else ord(c) - ord('a'))
    else:
        return None

def shift(i, n):
    return 0 if i is None else ((i + n + 26) % 26 - i)

def rot(s, n):
    return "".join(chr(ord(c) + shift(off(c), n)) for c in s)

    print rot(v, k)
def ask(question):
    return raw_input(question)


def secret():
    message = ask('Enter your message: ')
    number = int(ask('Enter a number: '))


def main():
   code = secret()
   print(code) 

if __name__ == '__main__':
    code = secret()
    print(code)
