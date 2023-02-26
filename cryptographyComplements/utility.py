def isOdd(number):
    "Check, from a number, given in input, if the number is odd."
    number = str(number)
    odds = ("1","3","5","7","9")
    if number.endswith(odds):
        return True
    return False

def isEven(number):
    "Check, from a number, given in input, if the number is even."
    number = str(number)
    evens = ("0", "2", "4", "6", "8")
    if number.endswith(evens):
        return True
    return False

def isNumber(*args):
    "Check if the input entered, can be converted to a number, or contains other characters."
    check = []
    for arg in args:
        try:
            arg = int(arg)
            checkNum = True

        except ValueError as e:
            print(f"Cryptography Complements: {e}")
            checkNum = False
        
        check.append(checkNum)

    if False in check:
        print(f"Cryptography Complements: One or more input, are not numbers.")
        return False

    return True