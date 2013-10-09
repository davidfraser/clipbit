from unittest2 import TestCase

from clipbit import secretcodes


class SecretCodesTestCase(TestCase):

    def test_shift(self):
        self.assertEquals(
            '',
            secretcodes.shift(1,2,3)
        )

    def test_encode(self):
        self.assertEquals(
            'ifmmp', 
            secretcodes.encode('hello', 1)
        )

    def test_decode(self):
        self.assertEquals(
            'hello',
            secretcodes.decode('ifmmp', 1)
        )