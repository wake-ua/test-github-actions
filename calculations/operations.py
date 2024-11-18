def fibonacci(number: int) -> int:
    """
    Calculates the Fibonacci value for the desired number

    :param number: integer defining the desired position within the series
    :returns: the numeric value of the Fibonacci series
    :raises ValueError: raises an exception if the input value is
                        lower than zero
    """
    if number < 0:
        raise ValueError("Input number should be equal or greater than 0.")
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
