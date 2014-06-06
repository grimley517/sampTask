import task3 as t3
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        assert t3.getChkDig('0000000001')==9 #test1 fails tenth digit fail
        assert t3.getChkDig('0000000010')==8 #test1 Fails 9th digit check fail
        assert t3.getChkDig('0000000100')==7 #test1 Fails 8th digit check fail
        assert t3.getChkDig('0000001000')==6 #test1 Fails 7th digit check fail
        assert t3.getChkDig('0000010000')==5 #test1 Fails 6th digit check fail
        assert t3.getChkDig('0000100000')==4 #test1 Fails 5th digit check fail
        assert t3.getChkDig('0001000000')==3 #test1 Fails 4th digit check fail
        assert t3.getChkDig('0010000000')==2 #test1 Fails 3th digit check fail
        assert t3.getChkDig('0100000000')==1 #test1 Fails 2th digit check fail
        assert t3.getChkDig('1000000000')==0 #test1 Fails 1th digit check fail
    
    def test2(self):
        assert t3.getChkDig('0000200000')=='X' #test2 Fails digit check x fail
if __name__ == '__main__':
    unittest.main()
