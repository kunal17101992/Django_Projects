from django.urls import path
from profileapp import views

app_name = 'profileapp'

urlpatterns = [
    path('', views.profiledetail, name='userprofile'),
    path('members/', views.MemberList.as_view(), name='memberlist'),
    path('others/<int:pk>/', views.OtherProfile, name='otherprofile'),
    path('update/<int:pk>',views.ProfileUpdate.as_view(), name='profileupdate'),
    path('add/<int:pk>/', views.Friendrequestadd, name='friendadd'),
    path('cancel/<int:pk>/', views.Friendrequestcancel, name='friendcancel'),
    path('approve/<int:pk>/', views.Friendrequestapprove, name='friendapprove'),
    path('friendrequest/', views.Friendrequests, name='friendrequest'),
]
