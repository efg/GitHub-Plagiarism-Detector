# IMPORTS

# Creates and returns a json response with message (Status code, eg:200) and payload (data to be returned as part of the response)
def make_response(message, payload={}):
    response = {'message': message}
    if payload:
        response['payload'] = payload
    return response
