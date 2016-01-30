x = int(raw_input('Enter and integer: '))

for ans in range(abs(x) + 1):
    if ans**3 == x:
        break

if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube.')
else:
    if x < 0:
        ans = -ans
    print('The cube root of ' + str(x) + ' is ' + str(ans))
