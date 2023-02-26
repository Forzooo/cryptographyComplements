def EulerTotientFunction(number):
    "Calculate, from a given number, the Euler Totient function."

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