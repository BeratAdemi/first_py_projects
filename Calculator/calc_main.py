# This is a calculator!
import help

# Defining an introduction
def start():
    print 'Welcome! This is calculator offers the following functions:\n' \
        '\n' \
        'addition (add)\n' \
        'subtraction (sub)\n' \
        'multiplication (mul)\n' \
        'division (div)\n' \
        '\n' \
        'You call functions like this:\n' \
        '1. Enter the function you want to use (add/sub/div/mul) \n' \
        '2. Enter the first number \n' \
        '3. Enter the second number \n' \
        'If you need any further help call the function help.\n' \

    raw_input('Press Enter to start')
    return


def add(a, b):
    summ= a + b
    return summ


def sub(a, b):
    subt= a - b
    return subt


def div(a, b):
    divi= a / b
    return divi


def mul(a, b):
    mult= a * b
    return mult


def exit():
    return


def in_func():
    func = raw_input('Enter a function: ')
    return func


def in_num1():
    x = True
    while x:
        num1 = raw_input('Enter the first number: ')
        try:
            val = int(num1)
            x = False
        except ValueError:
            print 'This is not a number'

    return val


def in_num2():
    x = True
    while x:
        num2 = raw_input('Enter the second number: ')
        try:
            val = int(num2)
            x = False
        except ValueError:
            print 'This is not a number'

    return val

start()
run = True
while run:
    func = in_func()
    if func[0:4] == 'exit':
        print 'Thank you for using this program :)'
    elif func[0:4] == 'help':
        print 'Loading...'
    else:
        num1 = in_num1()
        num2 = in_num2()
    res = 0

    if func[0:3] == 'add':
        add_num1 = int(num1)
        add_num2 = int(num2)
        res = add(add_num1, add_num2)
        print res

    elif func[0:3] == 'sub':
        sub_num1 = int(num1)
        sub_num2 = int(num2)
        res = sub(sub_num1, sub_num2)
        print res

    elif func[0:3] == 'div':
        div_num1 = int(num1)
        div_num2 = int(num2)
        res = div(div_num1, div_num2)
        print res

    elif func[0:3] == 'mul':
        mul_num1 = int(num1)
        mul_num2 = int(num2)
        res = mul(mul_num1, mul_num2)
        print res

    elif func[0:4] == 'help':
        help.help()

    elif func[0:4] == 'exit':
        run = False

    else:
        print 'The function is not supported'


