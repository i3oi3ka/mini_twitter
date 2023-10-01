from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('user-detail/<int:user_id>', views.user_detail, name='user_detail')
]
