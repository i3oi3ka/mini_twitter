from django.db import models


# Створіть модель User в додатку "users".
# Ваша модель User повинна містити наступні поля: username, email, date_joined.
class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    date_joined = models.DateField(auto_now_add=True)

