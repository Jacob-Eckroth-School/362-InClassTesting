import unittest
import calc

class TestCase(unittest.TestCase):
    def test_add1(self):    #Adding ints        
        self.assertAlmostEqual(calc.add(1,2),3,4)
    def test_add2(self):
        self.assertAlmostEqual(calc.add(1.5,-3),-1.5,4) #Testing floating point and negative
    def test_add3(self):
        self.assertAlmostEqual(calc.add(0,5),5,4) #Testing 0
    def test_add4(self):
        self.assertAlmostEqual(calc.sub("hello world",3),4,None) #Testing strings
    def test_addFail(self):
        self.assertAlmostEqual(calc.add(2,2),5,4) #Should fail

    def test_sub1(self):    #subing ints        
        self.assertAlmostEqual(calc.sub(1,2),-1,4)
    def test_sub2(self):
        self.assertAlmostEqual(calc.sub(1.5,-3),4.5,4) #Testing floating point and negative
    def test_sub3(self):
        self.assertAlmostEqual(calc.sub(0,5),-5,4) #Testing 0
    def test_add4(self):
        self.assertAlmostEqual(calc.sub("hello world",3),4,None) #Testing strings
    def test_subFail(self):
        self.assertAlmostEqual(calc.sub(2,2),1,4) #Should fail

    def test_mul1(self):    #muling ints        
        self.assertAlmostEqual(calc.mul(1,2),2,4)
    def test_mul2(self):
        self.assertAlmostEqual(calc.mul(1.5,-3),-4.5,4) #Testing floating point and negative
    def test_mul3(self):
        self.assertAlmostEqual(calc.mul(0,5),0,4) #Testing 0
    def test_add4(self):
        self.assertAlmostEqual(calc.mul("hello world",3),4,None) #Testing strings
    def test_mulFail(self):
        self.assertAlmostEqual(calc.mul(2,2),3,4) #Should fail


    def test_div1(self):    #diving ints        
        self.assertAlmostEqual(calc.div(1.0,2.0),.5,4)
    def test_div2(self):
        self.assertAlmostEqual(calc.div(4.5,1.5),3.0,4) #Testing floating point and negative
    def test_div3(self):
        self.assertAlmostEqual(calc.div(5,0),None,4) #Testing 0
    def test_add4(self):
        self.assertAlmostEqual(calc.div("hello world",3),None,4) #Testing strings
    def test_divFail(self):
        self.assertAlmostEqual(calc.div(2,2),3,4) #Should fail



if __name__ == "__main__":
    unittest.main()