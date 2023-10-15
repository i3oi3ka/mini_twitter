from django.urls import path

from .views import PostListView, CommentListView, PostCreateView, PostDetailView, CommentCreateView, CommentDetailView, \
    like, PostUpdateView, PostDeleteView, LikedPostUserList, PostFollowListView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('like/<int:pk>', like, name='like'),
    path('liked_post_user/<int:pk>', LikedPostUserList.as_view(), name='liked_post_user'),
    path('posts_list_user/<int:user_id>', PostListView.as_view(), name='posts_list_user'),
    path('posts_follow_list/', PostFollowListView.as_view(), name='posts_follow_list'),
    path('create-post/', PostCreateView.as_view(), name='create_post'),
    path('update-post/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete-post/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('create-comment/<int:pk>', CommentCreateView.as_view(), name='create_comment'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('comments-list/<int:post_id>', CommentListView.as_view(), name='comments_list'),
    path('comment-detail/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
    path('comment-update/<int:pk>', CommentUpdateView.as_view(), name='comment_update'),
    path('comment-delete/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),
]

