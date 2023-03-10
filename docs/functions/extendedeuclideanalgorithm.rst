Extended Euclidean Algorithm
============================

This function, from two numbers given in input, calculates their MCD, and returns it as an integer.

Extended Euclidean Algorithm is faster than the Euclidean Algorithm. It uses the equation: au + bv = gcd(a,b).

.. code-block:: python

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

Note: ``isNumber`` function checks if the input entered is a number.
``isNumber`` can be found in Tools functions section.