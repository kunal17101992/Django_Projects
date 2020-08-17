"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from signup import views
from blog.views import PostList
from django.contrib.auth import views as Pass_Views
from django.contrib.auth.decorators import login_required
from socialmedia import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signin,name='signin'),
    path('login/', PostList.as_view(), name='signinhome'),
    path('logout/', views.signout,name='signout'),
    path('password-reset/', Pass_Views.PasswordResetView.as_view(template_name = 'signup/password_reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',Pass_Views.PasswordResetConfirmView.as_view(template_name='signup/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/done/', Pass_Views.PasswordResetDoneView.as_view(template_name='signup/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-complete/', Pass_Views.PasswordResetCompleteView.as_view(template_name='signup/password_reset_complete.html'),name='password_reset_complete'),
    path('password-change/', login_required(Pass_Views.PasswordChangeView.as_view(template_name='signup/password_change_form.html')),name='password_change_form'),
    path('password-change/done/', Pass_Views.PasswordChangeDoneView.as_view(template_name='signup/password_change_done.html'),name='password_change_done'),
    path('signup/', include('signup.urls')),
    path('profile/', include('profileapp.urls')),
    path('post/', include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
