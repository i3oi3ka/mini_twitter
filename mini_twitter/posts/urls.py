from django.urls import path
from .views import posts_list, comments_list, create_post, post_detail, create_comment, comment_detail

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('posts_list_user/<int:user_id>', posts_list, name='posts_list_user'),
    path('comments/', comments_list, name='comments_list'),
    path('create-post/', create_post, name='create_post'),
    path('create-comment/', create_comment, name='create_comment'),
    path('post-detail/<int:post_id>', post_detail, name='post_detail'),
    path('comments-list/<int:post_id>', comments_list, name='comments_list'),
    path('comment-detail/<int:comment_id>', comment_detail, name='comment_detail'),
]
