import src.export.html_generator


def test_generate_html_single_parameter():
    def calculate_square(x):
        return x * x

    result = src.export.html_generator.generate_html([1, 2, 3],
                                                     calculate_square)
    assert result == "<!DOCTYPE html>\n<html>\n\t<body>" \
                     "\n\t\t<h1>calculate_square</h1>"\
                     "\n\t\t<ul>" \
                     "\n\t\t\t<li>calculate_square(1) = 1</li>" \
                     "\n\t\t\t<li>calculate_square(2) = 4</li>" \
                     "\n\t\t\t<li>calculate_square(3) = 9</li>" \
                     "\n\t\t</ul>" \
                     "\n\t</body>\n</html>"


def test_generate_html_multi_parameter():
    def calculate_sum(x, y):
        return x + y

    input_list = [(1, 2), (3, 4)]
    result = src.export.html_generator.generate_html(input_list,
                                                     calculate_sum)
    assert result == "<!DOCTYPE html>\n<html>\n\t<body>" \
                     "\n\t\t<h1>calculate_sum</h1>"\
                     "\n\t\t<ul>" \
                     "\n\t\t\t<li>calculate_sum(1, 2) = 3</li>" \
                     "\n\t\t\t<li>calculate_sum(3, 4) = 7</li>" \
                     "\n\t\t</ul>" \
                     "\n\t</body>\n</html>"
