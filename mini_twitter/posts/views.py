from django.shortcuts import render

from posts.models import Post, Comment


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})


def comments_list(request):
    comments = Comment.objects.all()
    return render(request, 'posts/comments_list.html', {'comments': comments})
