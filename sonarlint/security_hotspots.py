def cors():
    from django.http import HttpResponse
    response = HttpResponse("OK")
    response["Access-Control-Allow-Origin"] = "*"
