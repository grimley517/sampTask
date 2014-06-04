import task1 as t1
import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):
        '''
        this setup sets an initial state for the rates.
        '''
        self.rates = {'EUR':1.5, 'USD':2, 'JPY':100}
        for symbol in self.rates:
            t1.setRate(symbol,self.rates[symbol])

    def test1(self):
        '''this test is to check the set ability of conversion rates'''
        rates = {'EUR':1.23, 'USD':1.67, 'JPY':171.95}
        t1.setRate('EUR',rates['EUR'])
        assert (t1.getRate('EUR') == rates['EUR'])#Test 1 fails  - EUR rate does not set
        t1.setRate('USD',rates['USD'])
        assert (t1.getRate('USD') == rates['USD'])#Test 1 fails  - USD rate does not set
        t1.setRate('JPY',rates['JPY'])
        assert (t1.getRate('JPY') == rates['JPY'])#Test 1 fails  - JPY rate does not set  
        t1.setRate('GBP', 2)
        assert (t1.getRate('GBP') == 1) #test 1 fails - GBP rate should not be changable
        
    def test2(self):
        ''' 
        this test is to test conversion into GBP using the rates from the setup value
    
        '''
        assert (t1.convert('EUR','GBP',3)==2)#test 2 fails - euro conversion
        assert (t1.convert('USD','GBP',6)==3)#test 2 fails - dollar conversion
        assert (t1.convert('JPY','GBP',200)==2)#test 2 fails - yen conversion
    
    def test3(self):
        '''
        This test is to test conversion from GBP to other currencies
        '''
        assert (t1.convert('GBP','EUR',1)==1.5)#test 3 fails - euro conversion
        assert (t1.convert('GBP','USD',2)==4)#test 3 fails - dollar conversion
        assert (t1.convert('GBP','JPY',3)==300)#test 3 fails - yen conversion
        
    def test4(self):
        '''
        This test is to test conversion from between other currencies
        '''
        assert (t1.convert('JPY','EUR',100)==1.5)#test 3 fails yen - euro conversion
        assert (t1.convert('EUR','USD',3)==4)#test 3 fails euro - dollar conversion
        assert (t1.convert('USD','JPY',6)==300)#test 3 fails dollar - yen conversion
        
if __name__ == '__main__':
    unittest.main()
