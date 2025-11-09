from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя, где email используется для авторизации,
    а также добавлены avatar, phone_number и country.
    """
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    # используем email как поле для входа
    USERNAME_FIELD = 'email'
    # username оставляем обязательным при создании через createsuperuser,
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
