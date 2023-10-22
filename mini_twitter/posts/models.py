from django.db import models
from django.urls import reverse
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True, related_name='liked_post')
    image = models.ImageField(upload_to='posts/image', blank=True, null=True)

    def __str__(self):
        return f'Post: {self.title}, created: {self.created_at}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
