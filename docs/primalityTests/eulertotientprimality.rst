Euler Totient Primality Test
============================
This primality test use the equality of: ``number - 1 = phi(number)`` where phi is the ``Euler Totient Function``, available in Maths functions.
And if the equality is true than the number entered in input is a prime number, because a prime number has many relatively primes as many as the prime - 1.

.. code-block:: python

    from cryptographyComplements.mathFunctions import EulerTotientFunction
    from cryptographyComplements.tools import isNumber
    def EulerTotientPrimalityTest(n: int):
        "Using the equation: p - 1 = phi(p), you can verify if a number is prime. \nThis primality test is 100% valid but numbers greater than 2^60 requires to much time, and computational power, to be calculated using this primality test."

        if n < 0 and not isNumber(n): # verifying if the input is a number and belongs to N
            return None
        

        phi = EulerTotientFunction(n)

        if (n - 1) == phi:
            print("Cryptography Complements: The number entered is prime")
            return True
        
        print("Cryptography Complements: The number entered is not a prime")
        return False

The following table reports the number used to see the maximum large number that can be verified using this primality test.
The numbers below are randomly generated between two power of 2.

The **execution time**, it's for the **single prime only**, not for all the randomly generated numbers.


+-----------------+---------------------+-----------------+
| Number between: | Prime obtained:     | Execution time: |
+=================+=====================+=================+
| 2^50 and 2^51   | 1306468461935911    | 00:00:3.194     |
+-----------------+---------------------+-----------------+
| 2^55 and 2^56   | 55213038842602453   | 00:00:21.241    |
+-----------------+---------------------+-----------------+
| 2^56 and 2^57   | 142500755154440311  | 00:00:34.188    |
+-----------------+---------------------+-----------------+
| 2^59 and 2^60   | 675545629734934219  | 00:01:15.655    |
+-----------------+---------------------+-----------------+
| 2^62 and 2^63   | 5583619628687934733 | 00:06:19.319    |
+-----------------+---------------------+-----------------+


If you want to replicate this, you can use this code:

.. code-block:: python

    import random
    from cryptographyComplements.tools import isNumber, startChronometer, stopChronometer
    from cryptographyComplements.primalityTests import EulerTotientPrimalityTest

    minN, maxN = 2**62, 2**63 # select the power of 2 that you prefer

    stopwatchTotal = startChronometer()

    while True:
        stopwatchNumber = startChronometer()
        n = random.randint(minN, maxN)

        if EulerTotientPrimalityTest(n):
            break

    print(f"Total execution time: {stopChronometer(stopwatchTotal)}")
    print(f"Number: {n} verify took: {stopChronometer(stopwatchNumber)}")

    # print((minN) < n < (maxN)) # Use this only if you want to be sure that the number has been generated between minN and maxN