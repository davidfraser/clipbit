Secret Codes
============

To get this to work, enter a message and then a number between ``1`` and ``25`` (like ``3``). You will then receive a secret code for that message! To decode the message, you need to put in the secret code you got out, and then make the number a *minus* the first number you put in (like ``-3``). You can use this to decode a secret code you get from a friend...

.. code:: python

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


