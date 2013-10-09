from unittest2 import TestCase

from clipbit import secretcodes


class SecretCodesTestCase(TestCase):

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