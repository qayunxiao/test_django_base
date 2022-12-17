# -*- coding: utf-8 -*-
# @Time    : 2022/12/16 10:57
# @Author  : alvin
# @File    : test_sample.py
# @Software: PyCharm
import unittest

def add(a,b):
    return a+b

def setUpModule():
    print("模块开始")
def tearDownModule():
    print("模块结束")
#测试类必须继承unittest.TestCase
class MyTest(unittest.TestCase):
    def setUp(self):
        print("case 开始 创建测试数据")
    @classmethod
    def setUpClass(cls) -> None:
        print("类级别 case 开始 创建测试数据")
    #测试用例必须要test开头 TestLoader类方法testMethodPrefix变量
    def test_case_add1(self):
        print("test_case_add1")
        result = add(1,2)
        self.assertEqual(result,3)

    def test_case_add2(self):
        print("test_case_add2")
        result = add(1.1,2.2)
        self.assertNotEqual(result,3.3)
    def test_case_in3(self):
        self.assertIn("hello","hello world!")

    def tearDown(self) :
        print("case 结束 删除测试数据")
    # -> None py3.5写法 写不写都可以
    @classmethod
    def tearDownClass(cls) -> None:
        print("类级别case 结束 删除测试数据")

if __name__ == '__main__':
    unittest.main()

    #测试套件
    # suit= unittest.TestSuite()
    # suit.addTest(MyTest("test_case_add1"))
    # suit.addTest(MyTest("test_case_add2"))
    # suit.addTest(MyTest("test_case_in3"))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)