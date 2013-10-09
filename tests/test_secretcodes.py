from unittest2 import TestCase

from clipbit import secretcodes


class RotTestCase(TestCase):
    def test_rot(self):
        self.assertEquals(
            'ifmmp', 
            secretcodes.rot('hello', 1)
        )
