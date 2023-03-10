Euclidean Algorithm
===================

This function, from two numbers given in input, calculates their MCD, and returns it as an integer.

.. code-block:: python

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

Note: ``isNumber`` function checks if the input entered is a number.
``isNumber`` can be found in Tools functions section.