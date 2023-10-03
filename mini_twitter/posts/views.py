from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Post, Comment

from .forms import PostForm, CommentForm
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# def posts_list(request, user_id=None):
#     comment_count = dict()
#     if user_id:
#         posts = Post.objects.filter(user__id=user_id)
#     else:
#         posts = Post.objects.all()
#     if posts:
#         for post in posts:
#             comment_count[str(post.pk)] = Comment.objects.filter(post__id=post.pk).count()
#     return render(request, 'posts/posts_list.html', {'posts': posts, 'comment_count': comment_count})


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        if self.kwargs.get('user_id'):
            posts = Post.objects.filter(user__id=self.kwargs['user_id'])
        else:
            posts = Post.objects.all()
        return posts

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_count = dict()
        if context['posts']:
            for post in context['posts']:
                comment_count[post.pk] = Comment.objects.filter(post__id=post.pk).count()
        context['comment_count'] = comment_count
        return context


# def comments_list(request, post_id):
#     comments = Comment.objects.filter(post__id=post_id)
#     post = get_object_or_404(Post, pk=post_id)
#     context = {
#         'comments': comments,
#         'post': post
#     }
#     return render(request, 'posts/comments_list.html', context)


class CommentListView(ListView):
    model = Comment
    template_name = 'posts/comments_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        comments = Comment.objects.filter(post__id=self.kwargs['post_id'])
        return comments

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return context


# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()
#             return redirect('post_detail', post_id=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'posts/create_post.html', {'form': form})

class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'


# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     comments = Comment.objects.filter(post__id=post_id)
#     context = {"post": post, 'count_comments': len(comments)}
#     return render(request, "posts/post_detail.html", context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_comments'] = Comment.objects.filter(post__id=self.kwargs['pk']).count()
        return context


# def create_comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save()
#             return redirect('comment_detail', comment_id=comment.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'posts/create_comment.html', {'form': form})

class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'posts/create_comment.html'


# def comment_detail(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     context = {'comment': comment}
#     return render(request, 'posts/comment_detail.html', context)

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'posts/comment_detail.html'
    context_object_name = 'comment'