from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.validators import ValidationError

from .handlers import UserHandler
from .utils import response

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            user_handler = UserHandler()
            status, message, data = user_handler.create(request)
        except ValidationError as error:
            status, message, data = HTTP_403_FORBIDDEN, "Validation error", error.detail
        except ValueError or TypeError or IntegrityError as error:
            status, message, data = HTTP_400_BAD_REQUEST, "Bad request", dict()
        except Exception as error:
            status, message, data = HTTP_400_BAD_REQUEST, "Something Went Wrong", dict()
        finally:
            return response(status, message, data)