#编写单元测试,需要引入Python自带的unittest模块,
#单元测试是用来对一个模块 一个函数或者一个类来进行正确性检验的测试工作
#单元测试是用来对一个模块 一个函数或者一个类来进行正确性检验的测试工作
import unittest

class Dict(dict):
    def __init(self):
        super.__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

#编写单元测试时,需要编写一个测试类,该类从unittest.TestCase继承,
#以test开头的方法是测试方法,不以test开头的方法不被当成测试方法,测试的时候不会执行
#由于unittest.TestCase提供了很多内置的条件判断,所以只需要调用这些方法就可以断言输出是否符合预期.最常用的断言:assertEqual()\assertTrue()
#可以在单元测试中编写setUp与tearDown
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setup test.')

    def tearDown(self):
        print('teardown test.')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d= Dict()
        d['key'] = 'value'
        self.assertTrue('key' in d.keys())
        self.assertEqual(d['key'], 'value')

    def hello(self):
        print("hello")

#运行单元测试
if __name__=='__main__':
    unittest.main()

