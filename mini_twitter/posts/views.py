from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from posts.models import Post, Comment

from posts.forms import PostForm, CommentForm


def posts_list(request, user_id=None):
    if user_id:
        posts = Post.objects.filter(user__id=user_id)
    else:
        posts = Post.objects.all()
    if posts:
        comment_count = dict()
        for post in posts:
            comment_count[str(post.pk)] = Comment.objects.filter(post__id=post.pk).count()
        print(comment_count)
    return render(request, 'posts/posts_list.html', {'posts': posts, 'comment_count': comment_count})


def comments_list(request, post_id):
    comments = Comment.objects.filter(post__id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'comments': comments,
        'post': post
    }
    return render(request, 'posts/comments_list.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post__id=post_id)
    context = {"post": post, 'count_comments': len(comments)}
    return render(request, "posts/post_detail.html", context)


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', comment_id=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/create_comment.html', {'form': form})


def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    context = {'comment': comment}
    return render(request, 'posts/comment_detail.html', context)
