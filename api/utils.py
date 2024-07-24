from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

def response(status=HTTP_400_BAD_REQUEST, message=None, data=None):
    body = {
        'message': message,
        'data': data
    }
    return Response(status=status, data=body)