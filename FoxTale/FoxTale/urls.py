"""
URL configuration for FoxTale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from main import views as main_views
from user import views as user_views
from news import views as news_views
from support import views as support_view


from user import forms as user_forms

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.homeView , name='home'),
    path('register/', user_views.RegistrationUserView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True ,template_name='login.html', authentication_form=user_forms.UserLoginForm), name='login'),
    path('logout/', user_views.logout_without_confirm, name='logout'),
    path('profile/', user_views.ProfileView, name='profile'),

    path('news/', news_views.NewsView.as_view(), name='news'),
    path('news/<int:pk>/', news_views.NewsDetailView.as_view(), name='detail_new'),
    path('news/create_news/', news_views.NewsCreateView.as_view(), name='add_new'),
    path('news/<int:pk>/update/', news_views.NewsUpdateView.as_view(), name='new_update'),

    path('support/', support_view.CreateRoomView.as_view(), name='create_chat'),
    path('support/<int:pk>/', support_view.ChatRoomDetailView, name='support_chat'),
    path('support_list/', support_view.ChatListView.as_view(), name='support_list'),
    path('MyRequests/', support_view.UsersRequests.as_view(), name='user_requests'),
    path('completed_requests/', support_view.CompletedRequests.as_view(), name='completed_requests'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
