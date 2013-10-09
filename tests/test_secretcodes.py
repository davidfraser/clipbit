from unittest2 import TestCase

from clipbit import secretcodes


class RotTestCase(TestCase):
    def test_rot(self):
        self.assertEquals(
            'ifmmp', 
            secretcodes.encode('hello', 1)
        )

    def test_rot_decode(self):
        self.assertEquals(
            'hello',
            secretcodes.decode('ifmmp', 1)
        )