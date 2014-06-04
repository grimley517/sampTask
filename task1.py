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

def menuChoice():
    choice = None
    choices = ['change exchange rates', 'convert a value into another currency', 'exit']
    print ('Please choose a choice from the menu:')
    for i,c in enumerate(choices):
        print ('press {0} to {1}'.format(i,c))
    while choice not in range(len(choices)):
        choice = input ('Please select from the list {0} '.format(range(len(choices))))
    print ('\n ------------------\n')
    return (choice)
    
def chgRates():
    symbols = rates.keys()
    symbols.remove('GBP')#Pounds should not be changed
    print ('which rate do you wish to change?')
    for i, symbol in enumerate(symbols):
        print ('Enter {0} for {1}'.format(i, symbol))
    choice = None
    while choice not in range(len(symbols)):
        choice = input ('please enter your choice, Please select from the list {0} '.format(range(len(symbols))))
    newRate = float(input('Please enter the new rate '))
    setRate(symbols[choice],newRate)
    print ('\n ------------------\n')
    
def cvrt():
    symbols = rates.keys()
    print ('which Currency do you wish to change from? ')
    for i, symbol in enumerate(symbols):
        print ('Enter {0} for {1}'.format(i, symbol))
    fromSym = None
    while fromSym not in range(len(symbols)):
        fromSym = input ('please enter your choice, Please select from the list {0} '.format(range(len(symbols))))
        fromSym = int(fromSym)
    fromSym = symbols[fromSym]
    
    print ('\n ------------------\n')
    
    print ('which Currency do you wish to change to? ')
    for i, symbol in enumerate(symbols):
        print ('Enter {0} for {1}'.format(i, symbol))
    toSym = None
    while toSym not in range(len(symbols)):
        toSym = input ('please enter your choice, Please select from the list {0} '.format(range(len(symbols))))
        toSym = int(toSym)
    toSym = symbols[toSym]
    
    print ('\n ------------------\n')
    
    value = float(input('Please enter the ammount of {0} you wish to change into {1}'.format(fromSym, toSym)))
    
    value = convert(fromSym, toSym, value)
    print ('Your converted ammount is {0} {1:.2f}'.format(toSym, value))
    print ('\n ------------------\n')

running = True
while running:
    selection = menuChoice()
    if selection == 0:
        chgRates()
    elif selection == 1:
        cvrt()
    else:
        running = False