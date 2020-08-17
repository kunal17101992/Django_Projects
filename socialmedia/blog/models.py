from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    postuser = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=300)
    Description = models.TextField(null=True,blank=True)
    Upload_Image = models.ImageField(upload_to='postimages/',blank=True)
    Upload_Video = models.FileField(upload_to='videos/',blank=True)
    Upoad_file = models.FileField(upload_to='files/',blank=True)
    Published_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.postuser.username + '-' + self.Title

    def get_absolute_url(self):
        return reverse('signinhome')


class Comment(models.Model):
    commentuser = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Comment = models.TextField()
    Upload_Image = models.ImageField(upload_to='commentimages/', blank=True)
    Upload_file = models.FileField(upload_to='commentfiles', blank=True)
    Published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Comment


class PostLike(models.Model):
    likeuser = models.ForeignKey(User,on_delete=models.CASCADE)
    postlike = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.postlike.Description
