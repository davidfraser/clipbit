"""
Secret Codes
============

You can use this program to send secret messages to a friend who also has it,
and they can use it to decode the messages so they can understand them.

To get this to work, enter a message and then a number between ``1`` and ``25``
(like ``3``).
You will then receive a secret code for that message!
To decode the message, you need to put in the secret code you got out,
and then make the number a *minus* the first number you put in (like ``-3``).
"""

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
