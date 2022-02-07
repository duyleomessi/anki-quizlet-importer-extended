#!/usr/bin/env python3

import unittest
import quizletimporter

class Test(unittest.TestCase):
    def testColorText(self):
        self.maxDiff = None
        tests = {
            "hello": '<p style="font-size: 50px;"><span style="color: red">h</span><span style="color: blue">e</span><span style="color: red">ll</span><span style="color: blue">o</span></p>',
            "ehllo": '<p style="font-size: 50px;"><span style="color: blue">e</span><span style="color: red">hll</span><span style="color: blue">o</span></p>',
            "": '<p style="font-size: 50px;"></p>',
            "  ": '<p style="font-size: 50px;"></p>',
            "eau": '<p style="font-size: 50px;"><span style="color: blue">eau</span></p>',
            "hlm": '<p style="font-size: 50px;"><span style="color: red">hlm</span></p>',
        }

        for k, v in tests.items():
            realResult = quizletimporter.colorText(k, 50)
            self.assertEqual(v, realResult)

if __name__ == '__main__':
    unittest.main()
