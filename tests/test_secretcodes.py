from unittest2 import TestCase

from clipbit import secretcodes


class SecretCodesTestCase(TestCase):

    def test_encode(self):
        self.assertEquals(
            'gfkkp', 
            secretcodes.encode('hello', 1)
        )
        code = secretcodes.encode('hello', 999999999)
        self.assertEquals(
            'hello',
            secretcodes.encode(code, 999999999)
        )

