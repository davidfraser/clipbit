import pygame as p,random
I = random.randint
p.init()
d = p.display
s = d.set_mode([64]*2)
B = []
P = 0
L = 5
e = I(0,70)
Y = p.Rect(0,0,8,8)
Q = s.fill
l = lambda z:(8*(z%9),8*(z/9))
m = lambda n:Q(0,Y.move(l(n)))
S = [-1,1,0,0]
N = 1
t = 9
while 1:
    Q(99)
    m(e)
    P = P+t
    B += [P]
    B = B[-L:]
    map(m,B)
    if P == e:
        L += 1
        e = I(0,70)
    if P in B[:-1] or P%9 == 8 or P&256 or P>71:
        break
    d.flip()
    p.time.wait(99)
    o = N
    for v in p.event.get():
        if v.type == 2:
            N = v.key-273
            if -1 < N-2+o < 3:
                t = S[::-1][N]+S[N]*9

