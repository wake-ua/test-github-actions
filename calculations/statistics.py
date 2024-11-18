def event_probability(event_outcomes: int, sample_space: int) -> float:
    """
    Returns probability percent in range [0-100%] rounded to one decimal place.
    :param event_outcomes: number of possible event outcomes
    :param sample_space: size of the sample space
    :return: probability percent
    """
    if sample_space <= 0:
        raise ValueError("Sample space size should be greater than zero")
    if sample_space < event_outcomes:
        raise ValueError("Event outcomes should be lower or equal than sample "
                         "space")
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)
