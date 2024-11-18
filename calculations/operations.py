
def fibonacci(number: int) -> int:

    if number < 0:
        raise ValueError("Invalid input 'number' parameter. Input number "
                         "should be equal or greater than 0.")
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
