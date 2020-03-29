import unittest

import siphash


class TestSiphash(unittest.TestCase):
    def test_siphash(self):
        data = b'hello world'
        seed = b'1234567812345678'
        self.assertEqual(siphash.siphash(data, seed), 0x89cb5e38dae0f000)


if __name__ == '__main__':
    unittest.main()
