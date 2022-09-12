from django.shortcuts import render
from app_reg.forms import userForm, profileForm
from app_reg.models import profileModel
from django.contrib.auth.models import User

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'app_reg/index.html')

def registration(request):

    registered = False
    if request.method == "POST":
        user_form = userForm(request.POST)
        profile_form = profileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = userForm()
        profile_form = profileForm()

    return render(request, 'app_reg/registration.html', {'user_form':user_form,
                                                        'profile_form':profile_form,
                                                        'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('app_reg:data'))
            else:
                return HttpResponse("Account not active")
        else:
            print(f"username: {username}, password: {password}")
            return HttpResponse("Invalid username/password")
    else:
        return render(request, 'app_reg/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_reg:index'))

@login_required
def data(request):
    data = User.objects.order_by('id')
    return render(request, 'app_reg/data.html', {'data':data})
