from django.urls import path
from .views import PostListView, CommentListView, PostCreateView, PostDetailView, CommentCreateView, CommentDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('posts_list_user/<int:user_id>', PostListView.as_view(), name='posts_list_user'),
    path('create-post/', PostCreateView.as_view(), name='create_post'),
    path('create-comment/', CommentCreateView.as_view(), name='create_comment'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('comments-list/<int:post_id>', CommentListView.as_view(), name='comments_list'),
    path('comment-detail/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
]
