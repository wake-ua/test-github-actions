from fastapi.responses import HTMLResponse
from src import function_runner
from fastapi import APIRouter

router = APIRouter()


@router.get("/function/{function}/{value}/html", tags=["function"])
async def read_item(function: str, value: int):
    match function:
        case "fibonacci":
            html_result = function_runner.get_fibonacci_series_html(value)
        case "event_probability":
            html_result = function_runner.get_event_probability_series_html(value)
        case _:
            html_result = "<!DOCTYPE html><html><body>" \
                          "<p>Undefined function<p>" \
                          "</body></html>"
    return HTMLResponse(html_result)
