from django.db import models

from mini_twitter.users.models import User


# Створіть модель Post в додатку "posts".
# Ваша модель Post повинна містити наступні поля: user (посилання на модель User), title, content, created_at.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Створіть модель Comment в додатку "posts".
# Ваша модель Comment повинна містити наступні поля: user (посилання на модель User), post (посилання на модель Post), content, created_at.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
