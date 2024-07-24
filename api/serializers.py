from rest_framework import serializers
from .models import User, Contact, Spam

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'email']
        read_only_fields = ['id']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone']
        read_only_fields = ['id']

class SpamNumberSerializer(serializers.ModelSerializer):
    marked_as_spam_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Spam
        fields = ['phone', 'reported_by']
        read_only_fields = ['reported_by']