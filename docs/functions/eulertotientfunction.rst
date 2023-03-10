Euler Totient Function
======================

This function takes an integer input and calculates the Euler Totient function, returning the number of relatively prime numbers to the input.

.. code-block:: python

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

Note: The function depends on the `isNumber()` function, which is not provided here.
