from cryptographyComplements.utility import isNumber # required, to check inputs entered by the user

def EulerTotientFunction(number):
    "Calculate, from a given number, the Euler Totient function."
    if not isNumber(number):
        return None

    result = int(number)
    p = 2
    while p * p <= number:
        if number % p == 0:
            while number % p == 0:
                number //= p
            result -= result // p
        p += 1
    if number > 1:
        result -= result // number
    return result

def EuclideanAlgorithm(a, b):
    "Given two numbers, a and b, calculate their MCD."
    if not isNumber(a, b):
        return None

    while True:
        r = a % b
        if r != 0:
            a, b, remainder = b, r, r # remainder = r needs to be kept, because if r = 0, then it will be stored back.
        else:
            return remainder


def baseDiscreteLogarithm(base, congruence, modulo):
    "Calculate, from given base, congruence and modulo, the discrete logarithm. \nWarning: The function won't stop even if there isn't a number that can resolve the discrete logarithm."
    if not isNumber(base, congruence, modulo):
        return None
    
    BASE, CONGRUENCE, MODULO = int(base), int(congruence), int(modulo)
    power = 0

    while True:
        number = base**power
        if number % MODULO == CONGRUENCE % MODULO:
            print(f"log{BASE} {power} \u2261 {CONGRUENCE} (mod {MODULO})")
            logarithm = [BASE, power, CONGRUENCE, MODULO]
            # return BASE, power, CONGRUENCE, MODULO
            return logarithm
        
        power += 1