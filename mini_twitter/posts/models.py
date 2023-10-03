from django.db import models
from django.urls import reverse
from users.models import User


# Створіть модель Post в додатку "posts".
# Ваша модель Post повинна містити наступні поля: user (посилання на модель User), title, content, created_at.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post: {self.title}, created: {self.created_at}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


# Створіть модель Comment в додатку "posts".
# Ваша модель Comment повинна містити наступні поля: user (посилання на модель User), post (посилання на модель Post), content, created_at.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk': self.pk})