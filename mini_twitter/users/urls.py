from django.urls import path


from .views import RegisterView, ChangeProfile, ChangeInfo, UserDetail, subscribe, unsubscribe
from .views import login_view, logout_view, UserList

urlpatterns = [
    path('user_list/', UserList.as_view(), name='users_list'),
    path('user-detail/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('auth/sign-up/', RegisterView.as_view(), name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('change-user-info/<int:pk>', ChangeInfo.as_view(), name='change_user_info'),
    path('change-profile/<int:pk>', ChangeProfile.as_view(), name='change_profile'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
]
