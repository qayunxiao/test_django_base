# -*- coding: utf-8 -*-
# @Time    : 2022/12/17 9:51
# @Author  : alvin
# @File    : run.py
# @Software: PyCharm
import unittest
# suit = unittest.TestSuite()
# suit.addTest(MyTest("test_case_add1"))
# suit.addTest(MyTest("test_case_add2"))
# suit.addTest(MyTestSub("test_case_sub1"))
# suit.addTest(MyTestSub("test_case_sub2"))
# runner =unittest.TextTestRunner()
# runner.run(suit)
suit=unittest.defaultTestLoader.discover("./case","test_*.py")
runner =unittest.TextTestRunner()
runner.run(suit)