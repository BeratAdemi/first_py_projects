# Importing my own help file
import help

'''
    FUNCTION
'''


# Defining an introduction
def start():
    print 'Welcome! This is calculator offers the following functions:\n' \
        '\n' \
        'addition (add)\n' \
        'subtraction (sub)\n' \
        'multiplication (mul)\n' \
        'division (div)\n' \
        'modulo (mod) \n' \
        '\n' \
        'You call functions like this:\n' \
        '1. Enter the function you want to use (add/sub/div/mul) \n' \
        '2. Enter the first number \n' \
        '3. Enter the second number \n' \
        'If you need any further help call the function help.\n'
    return


# Function for addition and returning the result
def add(a, b):
    summ = a + b
    return summ


# Function for subtraction and returning the result
def sub(a, b):
    subt = a - b
    return subt


# Function for Modulo
def mod(a, b):
    modu = a % b
    return modu


# Function for division and returning the result
def div(a, b):
    divi = a / b
    return divi


# Function for multiplication and returning the result
def mul(a, b):
    mult = a * b
    return mult


# Function for ending the program
def exit():
    return


# Getting user input for function that should be used, checking if input is a valid function and returning it
def in_func():
    funct = ''
    x = True
    while x:
        funct = raw_input('Enter a function: ')
        try:
            if funct == 'add' or funct == 'sub' or funct == 'div' or funct == 'mul' or funct == 'mod' or funct == 'help' or funct == 'exit':
                x = False
            else:
                print 'This function is not supported'
        except Exception:
            pass
    return funct


# Getting user input for the first number and checking, if input is an int; returning the input
def in_num1():
    val = 0
    x = True
    while x:
        number1 = raw_input('Enter the first number: ')
        try:
            val = int(number1)
            x = False
        except ValueError:
            print 'This is not a number'
    return val


# Getting user input for the second number and checking, if input is an int; returning the input
def in_num2():
    val = 0
    x = True
    while x:
        number2 = raw_input('Enter the second number: ')
        try:
            val = int(number2)
            x = False
        except ValueError:
            print 'This is not a number'
    return val

'''
    EXECUTED CODE
'''


# Calling the function start
start()

# Setting run as True, run = False will stop the program
run = True

# Code for the calculator
while run:
    # User input for the function
    func = in_func()
    # Checking if user input for numbers is needed or if help/exit is requested
    if func[0:4] == 'exit':
        print 'Thank you for using this program :)'
        run = False
        continue
    elif func[0:4] == 'help':
        print 'Loading...'
        help.help()
        continue
    else:
        # User input for numbers
        num1 = in_num1()
        num2 = in_num2()
    # Variable for the later printed results
    res = 0

    # Check which function was chosen and execute the function; printing the result if necessary
    if func[0:3] == 'add':
        add_num1 = num1
        add_num2 = num2
        res = add(add_num1, add_num2)
        print res

    elif func[0:3] == 'sub':
        sub_num1 = num1
        sub_num2 = num2
        res = sub(sub_num1, sub_num2)
        print res

    elif func[0:3] == 'div':
        div_num1 = num1
        div_num2 = num2
        res = div(div_num1, div_num2)
        rest = mod(div_num1, div_num2)
        print "{}  remainder {}".format(res, rest)

    elif func[0:3] == 'mod':
        mod_num1 = num1
        mod_num2 = num2
        res = mod(mod_num1, mod_num2)
        print res

    elif func[0:3] == 'mul':
        mul_num1 = num1
        mul_num2 = num2
        res = mul(mul_num1, mul_num2)
        print res

    else:
        print 'Unexpected error! Exiting program'
        run = False
