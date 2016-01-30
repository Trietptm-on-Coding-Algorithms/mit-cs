x = int(raw_input('Give me an integer: '))

output = ''

isNeg = x < 0
x = abs(x)

if x == 0:
    output = '0'

while x > 0:
    output = str(x % 2) + output
    x /= 2

if isNeg:
    output = '-' + output

print("Binary representation is: " + output)
