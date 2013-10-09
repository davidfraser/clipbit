ask = raw_input


def offset(c):
    if c.isalpha():
        return (ord(c) - ord('A') if c.isupper() else ord(c) - ord('a'))
    else:
        return None


def shift(i, n):
    return 0 if i is None else ((i + n + 26) % 26 - i)


def rotate(message, num):
    return ''.join(
        chr(ord(char) + shift(offset(char), num)) for char in message
    )


def encode(message, number):
    return rotate(message, number)


def decode(message, number):
    return rotate(message, -number)


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
