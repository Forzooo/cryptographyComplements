from cryptographyComplements.utility import isNumber # required, to check inputs entered by the user

def EulerTotientFunction(number):
    "Calculate, from a given number, the Euler Totient function."
    if not isNumber(number):
        return None

    result = number
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
    
    BASE, congruence, modulo = int(base), int(congruence), int(modulo)
    power = 0

    while True:
        number = base**power
        if number % modulo == congruence % modulo:
            print(f"log{BASE} {power} \u2261 {congruence} (modulo {modulo})")
            return BASE, power, congruence, modulo
        
        power += 1