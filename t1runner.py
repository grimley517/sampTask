'''
this is the runner for task 1 - this runner implements the tested functions in task1.py and wraps them in a menu system
'''
import task1 as t1

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
    symbols = t1.rates.keys()
    symbols.remove('GBP')#Pounds should not be changed
    print ('which rate do you wish to change?')
    for i, symbol in enumerate(symbols):
        print ('Enter {0} for {1}'.format(i, symbol))
    choice = None
    while choice not in range(len(symbols)):
        choice = input ('please enter your choice, Please select from the list {0} '.format(range(len(symbols))))
    newRate = float(input('Please enter the new rate '))
    t1.setRate(symbols[choice],newRate)
    print ('\n ------------------\n')
    
def cvrt():
    symbols = t1.rates.keys()
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
    
    value = t1.convert(fromSym, toSym, value)
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
