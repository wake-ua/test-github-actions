import src.function_runner


def test_get_fibonacci_series_html():
    result = src.function_runner.get_fibonacci_series_html(0)
    assert result == "<!DOCTYPE html>\n<html>\n\t<body>\n\t\t" \
                     "<h1>fibonacci</h1>\n\t\t<ul>\n\t\t</ul>" \
                     "\n\t</body>\n</html>"


def test_get_get_event_probability_series_html():
    result = src.function_runner.get_event_probability_series_html(3)
    assert result == "<!DOCTYPE html>\n<html>\n\t<body>\n\t\t" \
                     "<h1>event_probability</h1>\n\t\t<ul>\n\t\t\t" \
                     "<li>event_probability(0, 3) = 0.0</li>\n\t\t\t" \
                     "<li>event_probability(1, 3) = 33.3</li>\n\t\t\t" \
                     "<li>event_probability(2, 3) = 66.7</li>\n\t\t" \
                     "</ul>\n\t</body>\n</html>"
