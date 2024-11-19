import src.function_runner


def test_get_fibonacci_series_html():
    result = src.function_runner.get_fibonacci_series_html(0)
    assert result == "<!DOCTYPE html>\n<html>\n\t<body>\n\t\t" \
                     "<h1>fibonacci</h1>\n\t\t<ul>\n\t\t</ul>" \
                     "\n\t</body>\n</html>"
