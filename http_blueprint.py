import logging 

import azure.functions as func 

bp = func.Blueprint() 

@bp.route(route="default_template") 
@bp.route(route="sample1")
def default_template(req: func.HttpRequest) -> func.HttpResponse: 
    logging.info('Python HTTP trigger function processed a request.') 

    name = req.params.get('name') 
    if not name: 
        try: 
            req_body = req.get_json() 
        except ValueError: 
            pass 
        else: 
            name = req_body.get('name') 

    if name: 
        return func.HttpResponse( 
            f"Hello, {name}. This HTTP-triggered function " 
            f"executed successfully.") 
    else: 
        return func.HttpResponse( 
            "This HTTP-triggered function executed successfully. " 
            "Pass a name in the query string or in the request body for a" 
            " personalized response.", 
            status_code=200 
        )
def sample1(req: func.HttpRequest) -> func.HttpResponse: 
    logging.info('Python HTTP trigger function processed a request.') 
    return func.HttpResponse( 
        "This HTTP-triggered function executed successfully. " 
        "Pass a name in the query string or in the request body for a" 
        " personalized response."
    )
