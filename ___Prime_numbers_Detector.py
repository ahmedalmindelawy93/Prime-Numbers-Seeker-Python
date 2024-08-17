print("Hi, this is a python code that outputs prime numbers for a specific range")

___Maximum_Number=100

def ___Function_Number_Classification(___Number):
    if ___Number < 2:
        return False
    for ___index1 in range(2, int(___Number**0.5) + 1):
        if ___Number % ___index1 == 0:
            return False
    return True

def ___Function_Prime_Numbers_detector():

    ___Primes_Numbers = []

    for ___Number in range(___Maximum_Number):
        if ___Function_Number_Classification(___Number):
            # primes.append(num)
            print(___Number)

    return ___Primes_Numbers


___Primes_Numbers = ___Function_Prime_Numbers_detector()

