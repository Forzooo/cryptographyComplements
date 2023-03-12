Euler Totient Function
======================

This function takes an integer in input and calculates the Euler Totient function.
It returns the number of relatively prime numbers to the input.


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

Note: ``isNumber`` function checks if the input entered is a number.
``isNumber`` can be found in Tools functions section.