from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.PostCreate.as_view(), name='postcreate'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='postupdate'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='postdelete'),
    path('comment/<int:pk>', views.PostComment, name='comment'),
    path('comment/delete/<int:pk>/', views.CommentDelete, name='commentdelete'),
    path('like/<int:pk>/', views.PostLikes, name='postlike'),
    path('like/detail/<int:pk>/', views.PostLikesDetail, name='postlikedetail'),
    path('myposts/', views.MyPostList.as_view(), name='mypostlist'),
 ]
