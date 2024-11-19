def generate_html(input_values: list, function: callable) -> str:
    function_name = function.__name__
    html_text = "<!DOCTYPE html>\n<html>\n\t<body>"
    html_text += "\n\t\t<h1>{}</h1>".format(function_name)
    html_text += "\n\t\t<ul>"
    for input_value in input_values:
        html_text += "\n\t\t\t<li>{}({}) = {}</li>".format(function_name,
                                                           input_value,
                                                           function(input_value))
    html_text += "\n\t\t</ul>"
    html_text += "\n\t</body>\n</html>"
    return html_text