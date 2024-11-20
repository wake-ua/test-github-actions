from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.routers import function

app = FastAPI()
app.include_router(function.router)
client = TestClient(app)


def test_get_fibonacci_html():
    response = client.get("/function/fibonacci/3/html")
    assert response.status_code == 200
    assert response.text == "<!DOCTYPE html>\n<html>\n\t<body>\n\t\t" \
                            "<h1>fibonacci</h1>\n\t\t<ul>" \
                            "\n\t\t\t<li>fibonacci(0) = 0</li>" \
                            "\n\t\t\t<li>fibonacci(1) = 1</li>" \
                            "\n\t\t\t<li>fibonacci(2) = 1</li>" \
                            "\n\t\t</ul>\n\t</body>\n</html>"


def test_get_event_probability_html():
    response = client.get("/function/event_probability/3/html")
    assert response.status_code == 200
    assert response.text \
           == "<!DOCTYPE html>\n<html>\n\t<body>\n\t\t" \
              "<h1>event_probability</h1>\n\t\t<ul>" \
              "\n\t\t\t<li>event_probability(0, 3) = 0.0</li>" \
              "\n\t\t\t<li>event_probability(1, 3) = 33.3</li>" \
              "\n\t\t\t<li>event_probability(2, 3) = 66.7</li>" \
              "\n\t\t</ul>\n\t</body>\n</html>"


def test_get_bas_function_html():
    response = client.get("/function/bad_function/3/html")
    assert response.status_code == 200
    assert response.text == "<!DOCTYPE html><html><body>" \
                            "<p>Undefined function<p>" \
                            "</body></html>"
