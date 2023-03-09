isEven
======

"isEven" is a Tool function, that from one or more numbers entered in input, checks if the numbers entered are evens, and it returns to the user a dictionary with boolean values associated with the respective value.

Python function code:

.. code-block:: python

    def isEven(*args):
        "Check if one or more numbers, entered in input, are even."

        if not isNumber(args):
            return None

        evens, check = ("0", "2", "4", "6", "8"), {}
        for arg in args:
            if str(arg).endswith(evens):
                check[arg] = True
            else:
                check[arg] = False

        if False in check:
            print(f"Cryptography Complements: One or more numbers, are not evens: {check}")
            return False
        
        return True

Note: The ``isNumber`` function is used to check if all the entered inputs are numbers.