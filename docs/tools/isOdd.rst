isOdd
=====

"isOdd" is a Tool function, that from one or more numbers entered in input, checks if the numbers entered are odds, and it returns to the user a boolean value.

.. code-block:: python

    def isOdd(*args):
        "Check if one or more numbers, entered in input, are odd."

        if not isNumber(args):
            return None

        odds, check = ("1","3","5","7","9"), {}
        for arg in args:
            if str(arg).endswith(odds):
                check[arg] = True
            else:
                check[arg] = False

        if False in check.values():
            return False

        return True

Note: The ``isNumber`` function is used to check if all the entered inputs are numbers.