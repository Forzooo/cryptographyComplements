from cryptographyComplements.tools import isNumber # required, to check inputs entered by the user

def EulerTotientFunction(number: int):
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

def EuclideanAlgorithm(a: int, b: int):
    "Given two numbers, a and b, calculate their MCD."
    if not isNumber(a, b):
        return None

    a, b = int(a), int(b)

    while True:
        r = a % b
        if r != 0:
            a, b, remainder = b, r, r # remainder = r needs to be kept, because if r = 0, then it will be stored back.
        else:
            return remainder

def ExtendedEuclideanAlgorithm(a: int, b: int):
    "Given two numbers, a and b, calculate their MCD. \nThe Extended Euclidean Algorithm is faster than Euclidean Algorithm. It uses the equation: au + bv = gcd(a,b)"

    if not isNumber(a, b):
        return None
    a, b = int(a), int(b)

    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        r = a % b
        x = x0 - (a // b)*x1
        y = y0 - (a // b)*y1
        a, b, x0, x1, y0, y1 = b, r, x1, x, y1, y

    return a

def baseDiscreteLogarithm(base: int, congruence: int, modulo: int):
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