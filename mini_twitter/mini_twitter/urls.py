"""
URL configuration for mini_twitter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import consult_gpt.consult

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('message/', include('message.urls')),
    path('comment/', include('comment.urls')),
    path('chat_with_gpt/', consult_gpt.consult.chat_with_gpt, name='chat_with_gpt'),
    path('consult/', consult_gpt.consult.consult, name='consult'),
    path('', include('posts.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)