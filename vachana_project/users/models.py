
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Manager for CustomUser
    """
    def create_user(self, email, password, date_of_birth, **extra_fields):
        """
        Create and save a regular user with an email, password and date of birth.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)  # Normalize email
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)  # Encrypt password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, date_of_birth, **extra_fields):
        """
        Create and save a superuser with an email, password and date of birth.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, date_of_birth, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model which doesn't have a username, but has a unique email and a date_of_birth.
    """
    username = None  # Remove the username field
    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(verbose_name="Birthday", null=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
from django.db import models
from django.conf import settings

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('created', 'Created Vachana'),
        ('liked', 'Liked Vachana'),
        # You can add more activities here
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.get_activity_type_display()} at {self.timestamp}"



