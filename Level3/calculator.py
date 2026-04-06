# this calculator preforms the basic mathitatics operation + ,- ,* ,/ ,% ,pow

def add(a,b) : return a+b
def sub(a,b) : return a-b
def multply(a,b): return a*b
def divid(a,b) : return a/b if b != 0 else  print('0 can not be divisor')
def mod(a,b) : return a%b
def power_of(a,b) : return a**b

mapping = {'+' : add, '-': sub, '*': multply, '/':divid , '%': mod, '**':power_of}

num1=  int(input('enter the first number : '))
operator = input('operator: ')
num2 = int(input('the second number'))

if operator in mapping:
    result = mapping[operator](num1 , num2)

    print(result)
else:
    print('there is no this type of operation on this caluclator 50')

