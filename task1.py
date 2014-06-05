'''
The task here is to create a simple currency converter.

Exchange rates should be able to be changed regularly by the user.

The user should be able to enter an ammount, select the chosen currency, and the currency into which this should be converted

the ficure shown should be correct to two decimal places.
'''

rates = {'GBP':1,'EUR':1.1, 'USD':1.2, 'JPY':100}

def setRate(symbol, rate):
    valid1 = symbol in rates.keys()
    valid2 = symbol not in ['GBP']
    if valid1 and valid2:
        rates[symbol]=rate
    
def getRate(symbol):
    return (rates[symbol])
    
def convert(fromSym, toSym, value):
    pounds = value / rates[fromSym]
    return (pounds * rates[toSym])

'''

The above functions are tested using the functional tests in task1tests.py  below is the interface.

'''

