from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AuthUerManager


def user_image_path(instance, filename):
    ext = os.path.splitext(filename)[-1]
    now = str(time.time()).replace('.', '')
    return os.path.join('users', '{}-{}{}'.format(now, str(instance), ext))

class UserManager(AuthUerManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('電子郵件', unique=True)
    profile = models.ImageField(blank=True, null=True, upload_to=user_image_path)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def username(self):
        return self.email.split('@')[0]

    def __str__(self):
        return self.username