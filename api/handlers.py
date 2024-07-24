from rest_framework.validators import ValidationError
from rest_framework.status import HTTP_201_CREATED

from .serializers import UserSerializer

class UserHandler():
    def create(self, request):
        
        user_serializer = UserSerializer(data=request.data)
        
        if not user_serializer.is_valid():
            raise ValidationError(user_serializer.errors)
        
        user = user_serializer.save()
        status, message, data = HTTP_201_CREATED, "User registered successfully", user_serializer.data
        
        return status, message, data