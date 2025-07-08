import azure.functions as func
import logging

from .generate import subfunction_1   # <-- logic lives here

bp = func.Blueprint()

@bp.route(
    route="replaceMe",
    auth_level=func.AuthLevel.ANONYMOUS,
    methods=["GET", "POST"]
)
def replaceMe(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing replaceMe request…")

    # parse query or JSON
    name = req.params.get("name")
    if not name:
        try:
            name = req.get_json().get("name")
        except ValueError:
            name = None

    # call your pure-Python logic from generate.py 
    greeting = subfunction_1(name)

    return func.HttpResponse(greeting, status_code=200)
