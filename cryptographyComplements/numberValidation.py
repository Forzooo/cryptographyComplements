def isOdd(number):
    number = str(number)
    odds = ("1","3","5","7","9")
    if number.endswith(odds):
        return True
    return False

def isEven(number):
    number = str(number)
    evens = ("0", "2", "4", "6", "8")
    if number.endswith(evens):
        return True
    return False
