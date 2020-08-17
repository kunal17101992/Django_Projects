from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView
from .models import UserProfile, Friend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

@login_required
def profiledetail(request):
    userprofile = UserProfile.objects.get(user=request.user)
    friendcount = Friend.objects.filter(frienduser1=request.user).filter(friendstatus=True).count()
    return render(request,'profileapp/profile.html',{'userprofile':userprofile, 'friendcount':friendcount})

class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model=UserProfile
    fields=['Gender',
            'Date_of_Birth',
            'Location',
            'Marital_Status',
            'Profession',
            'Company',
            'College_Name',
            'School_Name',
            'Contact_no',
            'Language_known',
            'Religion',
            'Profile_photo'
    ]

@login_required
def OtherProfile(request,pk):
    userprofile = UserProfile.objects.get(user_id=pk)
    friendcount = Friend.objects.filter(frienduser1_id=pk).filter(friendstatus=True).count()
    return render(request,'profileapp/profile.html',{'userprofile':userprofile, 'friendcount':friendcount})


class MemberList(LoginRequiredMixin,ListView):
    template_name = 'profileapp/User_list.html'

    def get_queryset(self):
        return User.objects.exclude(id = self.request.user.id).exclude(is_staff = True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a_list = list(Friend.objects.filter(frienduser1=self.request.user).filter(friendstatus=False).filter(is_request_sent=True).values('frienduser2_id'))
        b_list = []
        for j in a_list:
            b_list.append(j['frienduser2_id'])
        print(b_list)
        context['friendsent_data'] = b_list

        c_list = list(Friend.objects.filter(frienduser1=self.request.user).filter(friendstatus=False).filter(is_request_sent=False).values('frienduser2_id'))
        d_list = []
        for k in c_list:
            d_list.append(k['frienduser2_id'])
        print(d_list)
        context['friendget_data'] = d_list
        e_list = list(Friend.objects.filter(frienduser1=self.request.user).filter(friendstatus=True).values('frienduser2_id'))
        f_list = []
        for m in e_list:
            f_list.append(m['frienduser2_id'])
        print(f_list)
        context['friend_data'] = f_list
        return context

@login_required
def Friendrequestadd(request, pk):
    f1 = Friend(frienduser1 = request.user, frienduser2_id = pk, friendstatus=False, is_request_sent=True)
    f1.save()
    f2 = Friend(frienduser1_id = pk, frienduser2 = request.user, friendstatus=False)
    f2.save()
    return redirect('profileapp:memberlist')

@login_required
def Friendrequestcancel(request, pk):
    f1 = Friend.objects.filter(frienduser1 = request.user).filter(frienduser2_id = pk)
    f1.delete()
    f2 = Friend.objects.filter(frienduser2 = request.user).filter(frienduser1_id = pk)
    f2.delete()
    return redirect('profileapp:memberlist')

@login_required
def Friendrequestapprove(request, pk):
    f1 = Friend.objects.filter(frienduser1 = request.user).get(frienduser2_id = pk)
    f1.friendstatus = True
    f1.save()
    f2 = Friend.objects.filter(frienduser2 = request.user).get(frienduser1_id = pk)
    f2.friendstatus = True
    f2.save()
    return redirect('profileapp:memberlist')

@login_required
def Friendrequests(request):
    a = Friend.objects.filter(frienduser1=request.user).filter(friendstatus=False).filter(is_request_sent=False)
    return render(request, 'profileapp/approve_list.html', {'a':a})
