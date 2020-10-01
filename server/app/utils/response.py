#IMPORTS

# Makes a json response with message and payload
def make_response(message, payload={}):
    response = {'message':message}
    if payload:
        response['payload'] = payload
    return response