import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

    def test11(self):
        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

    def test1(self):
        weekday = calculate(2017, 5, 9)
        self.assertEqual(weekday, 2)

    def test2(self):
        weekday = calculate(1791, 5, 3)
        self.assertEqual(weekday, 2)

    def test3(self):
        retcode = main(("--year", "1791", "-month", "5", "--day", "3",))
        self.assertEqual(retcode,0)

    def test4(self):
        retcode = main(("--year", "5", "--month", "5", "--day", "3"))
        self.assertEqual(retcode, 0)

if __name__ == '__main__':
    unittest.main()
