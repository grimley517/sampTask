import task1 as t1
import unittests

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        '''this test is to check the set ability of conversion rates'''
        rates = {'EUR':1.23, 'USD':1.67, 'JPY':171.95}
        t1.setRate('EUR',rates['EUR'])
        assert (t1.getRate('EUR') == rates['EUR'])#Test 1 fails  - EUR rate does not set
        
if __name__ == '__main__':
    unittest.main()
