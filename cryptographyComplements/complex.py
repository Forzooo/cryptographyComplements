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

def DiscreteLogarithm(base, congruence, modulo):
    "Calculate, from given base, congreunce and modulo, the discrete logarithm. \nWarning: The function won't stop even if there isn't a number that can resolve the discrete logarithm."
    if not isNumber(base, congruence, modulo):
        return None
    
    BASE, CONGRUENCE, MODULO = int(base), int(congruence), int(modulo)
    power = 0

    while True:
        number = base**power
        if number % MODULO == CONGRUENCE % MODULO:
            print(f"log{BASE} {power} \u2261 {CONGRUENCE} (mod {MODULO})")
            return BASE, power, CONGRUENCE, MODULO
        
        power += 1