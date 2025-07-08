import azure.functions as func
import logging

from .generate import build_greeting   # <-- logic lives here

bp = func.Blueprint()

@bp.route(
    route="testHttpLenferink",
    auth_level=func.AuthLevel.ANONYMOUS,
    methods=["GET", "POST"]
)
def testHttpLenferink(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing TestHttpLenferink request…")

    # parse query or JSON
    name = req.__params.get("name")
    if not name:
        try:
            name = req.get_json().get("name")
        except ValueError:
            name = None

    # call your pure-Python logic from generate.py 
    greeting = build_greeting(name)

    return func.HttpResponse(greeting, status_code=200)
