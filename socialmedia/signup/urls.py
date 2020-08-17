from django.urls import path
from signup import views

app_name = 'signup'

urlpatterns = [
    path('', views.Signup, name='sign_up'),
    path('verify/<str:emailkey>/', views.EmailVerification, name='EmailVerification'),
]
