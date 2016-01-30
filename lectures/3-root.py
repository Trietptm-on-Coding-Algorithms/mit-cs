# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# while guess <= x:
#     print("guess: " + str(guess))
#     print("calc : " + str(abs(guess**2 -x)))
#     if abs(guess**2 -x) < epsilon:
#         break
#     else:
#         guess += step
#
# if abs(guess**2 - x) >= epsilon:
#     print 'failed'
# else:
#     print 'succeeded: ' + str(guess)

# ============

# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# while guess <= x:
#     print("guess: " + str(guess))
#     print("calc : " + str(abs(guess**2 -x)))
#     if abs(guess**2 - x) >= epsilon:
#         guess += step
#
# if abs(guess**2 - x) >= epsilon:
#     print 'failed'
# else:
#     print 'succeeded: ' + str(guess)

# ============

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    print("guess: " + str(guess))
    print("calc : " + str(abs(guess**2 -x)))
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)