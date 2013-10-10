ask = raw_input


def make_map(i):
    d = {}
    letters = list("abcdefghijklmnopqrstuvwxyz")
    for p in range(25,0,-2):
        k = letters.pop(0)
        i, r = divmod(i, p)
        v = d[k] = letters.pop(r)
        d[v] = k
        V, K = v.upper(), k.upper()
        d[K] = V
        d[V] = K
    return d


def encode(message, n):
    d = make_map(n)
    return ''.join(d.get(c, c) for c in message)


def main():
    message = ask('Enter your message: ')
    number = int(ask('Enter a number: '))
    code = encode(message, number)
    print('Now, you can give your friend the encoded message: %s' % code)
    print('All they need to decode it, is the number you entered above')
    print('And this program :)')


if __name__ == '__main__':
    main()

