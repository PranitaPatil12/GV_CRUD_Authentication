from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def RegisterView(req):
    form=UserCreationForm()
    if req.method == 'POST':
        form=UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(req,'account/register.html',context)

def LoginView(req):
    if req.method == 'POST':
        un = req.POST.get('uname')
        pw = req.POST.get('pass')
        mail= req.POST.get('mail')

        user = authenticate(email=mail,username=un,password=pw)
        if user is not None:
            login(req,user)
            subject = 'welcome to GFG world'
            message = f'Hi {user.username}, thank you for registering .'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email ]
            send_mail(subject, message, email_from, recipient_list)
            print('mail send successfully')

            return redirect('lap_show')
        else:
            print('Invalid Credentials')
            messages.error(req,'Invalid Credentials')

    return render(req,'account/login.html')

def logoutview(req):
    logout(req)
    return redirect('login')
