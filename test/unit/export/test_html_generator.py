import src.export.html_generator


def test_generate_html():
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
