from src.calculations.operations import fibonacci
from src.calculations.statistics import event_probability
from src.export.html_generator import generate_html


def get_fibonacci_series_html(maximum: int) -> str:
    """
    Get the html string showing the Fibonacci calculations for the numbers up
    from zero to the selected maximum value
    :param maximum: limit for the series
    :return: html string
    """
    input_list = range(0, maximum)
    html = generate_html(input_list, fibonacci)
    return html


def get_event_probability_series_html(maximum: int) -> str:
    """
    Get the html string showing the event probability calculations for the
    numbers from zero to the selected maximum value as space size
    :param maximum: limit for the series
    :return: html string
    """
    input_list = [(i, maximum) for i in range(0, maximum)]
    html = generate_html(input_list, event_probability)
    return html
