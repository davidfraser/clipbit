def off(c):
    if c.isalpha():
        return (ord(c) - ord('A') if c.isupper() else ord(c) - ord('a'))
ask = raw_input
to_num = ord
to_str = chr
    else:
        return None

def shift(i, n):
    return 0 if i is None else ((i + n + 26) % 26 - i)


def encode(message, number):
    return rot(message, number)


def decode(message, number):
    return rot(message, -number)
def rotate(message, num):
    return ''.join(
        to_str(to_num(char) + shift(offset(char), num)) for char in message
    )





def secret():
    message = ask('Enter your message: ')
    number = int(ask('Enter a number: '))
    return encode(message, number)


def main():
   code = secret()
   print('Now, you can give your friend the encoded message: %s' % code)
   print('All they need to decode it, is the number you entered above')
   print('And this program :)')


if __name__ == '__main__':
    main()
