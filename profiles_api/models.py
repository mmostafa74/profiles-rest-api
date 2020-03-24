from django.db import models
#standard base classes used to overriding  default django user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:   #checking if the user provided email address or not
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) #checking the second half of the email address to validate the email
        user = self.model(email=email, name=name)   #creating db model for a user

        user.set_password(password) #add password hashed to db
        user.save(using=self._db)   #define which db to use

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #overriding default model and add email address
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """retrun string representation of our user"""
        return self.email
    
    