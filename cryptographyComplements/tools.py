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

    if False in check.values():
        return False
    
    return True

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
            check[arg] = False
        
    if False in check.values():
        return False

    return True


class stopwatch:
    "Create as many stopwatch as you need."
    def start():
        "Start a stopwatch. \nNote: The chronometer needs to be saved into a variable."
        import time
        return time.time()

    def stop(startTimer):
        "Stop a given chronometer, and prints out how much it took."
        import time
        elapsed = time.time() - startTimer
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        print(f"Execution time: {int(hours):0>2}:{int(minutes):0>2}:{seconds:05.3f}")
        return elapsed