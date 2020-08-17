from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):

    gender_choice = [('Male','Male'),('Female','Female'),('Custom','Custom')]
    status_choice = [('Single','Single'),('Married','Married'),('In Relationship','In Relationship'),('Divorced','Divorced')]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Gender = models.CharField(choices=gender_choice, max_length=100,null=True,blank=True)
    College_Name = models.CharField(max_length=300,null=True,blank=True)
    School_Name = models.CharField(max_length=300,null=True,blank=True)
    Marital_Status = models.CharField(choices=status_choice, max_length=300,null=True,blank=True)
    Profession = models.CharField(max_length=300,null=True,blank=True)
    Company = models.CharField(max_length=300,null=True,blank=True)
    Location = models.CharField(max_length=300,null=True,blank=True)
    Date_of_Birth = models.DateField(null=True,blank=True)
    Language_known = models.CharField(max_length=300,null=True,blank=True)
    Religion = models.CharField(max_length=300,null=True,blank=True)
    Contact_no = models.IntegerField(null=True,blank=True)
    Profile_photo = models.ImageField(upload_to='profile_images/',blank=True)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('profileapp:userprofile')

class Friend(models.Model):
    frienduser1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='f1')
    frienduser2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='f2')
    friendstatus = models.BooleanField()
    is_request_sent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.frienduser1) + ' ' + str(self.frienduser2)
