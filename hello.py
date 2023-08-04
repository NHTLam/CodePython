# python artihmetic operations: +, -, *, /, //, %, **
a = int(input('Enter a: '))
b = int(input('Enter b: '))

print(f'{a:2} + {b:2} = {a + b:3}')
print('{:2} - {:2} = {:3}'.format(a, b, a-b))
print(f'{a:2} * {b:2} = {a * b:3}')
print(f'{a:2} / {b:2} = {a / b:3}')
print(f'{a:2} // {b:1} = {a // b:3}')
print(f'{a:2} % {b:2} = {a % b:3}')
print(f'{a:2} ** {b:1} = {a ** b:3}')
