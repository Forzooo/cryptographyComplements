isNumber
========

"isNumber" is a Tool function, that from one or more inputs, checks if them are numbers, and it returns to the user a dictionary with boolean values associated with the respective value.

Python function code:

.. code-block:: python

    def isNumber(*args):
        "Check if the input entered, can be converted to a number, or contains other characters."
        check = {}
        new_args = []
        for arg in args:
            if isinstance(arg, tuple):
                new_args.extend(arg)
            else:
                new_args.append(arg)

        for arg in new_args:
            try:
                arg = int(arg)
                check[arg] = True

            except ValueError as e:
                print(f"Cryptography Complements: {e}")
                check[arg] = False
            
        if False in check.values():
            print(f"Cryptography Complements: One or more input, are not numbers: {check}")
            return False

        return True