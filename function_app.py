import azure.functions as func
import logging

# import your new blueprint
from Functions.testHttpLenferink import bp as test_http_bp
from Functions.replaceMe import bp as replace_me_bp

app = func.FunctionApp() 

# wire it in
app.register_functions(test_http_bp) 
app.register_functions(replace_me_bp)


# Functie die kan worden gebruikt om te testen of de functie-app draait
@app.route(route="test", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Functie app is test draaiend.", status_code=200)