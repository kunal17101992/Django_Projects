from django.shortcuts import render,redirect
from .forms import SignUpForm,SigninForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.signing import TimestampSigner
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from profileapp.models import UserProfile, Friend
from django.contrib.sessions.models import Session


def Signup(request):
    msg = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User(
                username=request.POST.get('Username').lower(),
                password=request.POST.get('Password'),
                first_name=request.POST.get('First_Name'),
                last_name=request.POST.get('Surname'),
                email=request.POST.get('Emailid').lower(),
                is_active=False
            )
            user.set_password(user.password)
            signer = TimestampSigner()
            subject = 'Social Media Account verification mail'
            body = 'Hi ' + user.first_name + ',' + '\n\nPlease click on the link http://127.0.0.1:8000/signup/verify/' + signer.sign(user.email) + ' to activate your account.\n\nThanks,\nSocial Media Team'
            send_mail(subject,body,'skunal949@gmail.com',[user.email],fail_silently=False)
            user.save()
            profile = UserProfile(user=user,Gender=request.POST.get('Gender'))
            profile.save()
            msg='Successfully Signup!.Link has been sent to emailid for verification. It is valid for 30 minutes'
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html',{'form':form,'msg':msg})


def EmailVerification(request,emailkey):
    emailcheck = emailkey[0:emailkey.find(':')]
    usercount=User.objects.filter(email=emailcheck).filter(is_active=True).count()
    if usercount > 0:
        return HttpResponse('<h2>Your emailid has already verified.<a href="/">Click here to login</a></h2>')
    signer = TimestampSigner()
    try:
        emailid = signer.unsign(emailkey, max_age=600)
    except:
        return HttpResponse('<h2>Link has been expired. <a href="/password-reset">Click here to activate account</a></h2>')
    else:
        a = get_object_or_404(User, email=emailid)
        a.is_active = True
        a.save()
        return HttpResponse('<h2>Your email id has been verified.<a href="/">Click here to login</a></h2>')

def signin(request):
    if request.session.has_key(request.user.username):
        return redirect('signinhome')

    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['Username'])
            user = authenticate(username=form.cleaned_data['Username'].strip().lower(),password=form.cleaned_data['Password'])
            login(request,user)
            request.session[request.user.username] = True
            return redirect('signinhome')
    return render(request, 'signup/login.html', {'form':form})

@login_required
def signout(request):
    logout(request)
    return redirect('signin')
