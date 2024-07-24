from django.contrib.auth.models import BaseUserManager

"""
DAL(Data Access Layer) file will be used to perform all database operations.
This helps in seperating database operations and business logics.
"""

class UserManager(BaseUserManager):
    def create_user(self, phone, name, password, email=None):
        # if not phone:
        #     raise ValueError("Users must have a phone number")
        # if not name:
        #     raise ValueError("Users must have a name")
        # if not password:
        #     raise ValueError("Users must have a password")
        
        user = self.model(
            phone = phone,
            name = name,
            email = email
        )
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, phone, name, password, email=None):
        user = self.create_user(phone, name, password, email)
        user.is_admin = True
        user.save()
        return user