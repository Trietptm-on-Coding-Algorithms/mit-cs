varA = 'moo'
varB = 'python'

if (type(varA) == type('')) or (type(varB) == type('')):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")
