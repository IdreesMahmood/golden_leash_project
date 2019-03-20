from django.shortcuts import render, redirect
from golden_leash.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from golden_leash.models import UserProfile

# Create your views here.

def index(request):

    return render(request, "golden_leash/index.html", {})

def walkerProfiles(request):
    profiles = UserProfile.objects.all()
    context_dict = {'profiles': profiles}
    return render(request, "golden_leash/walkerProfiles.html", context=context_dict)

def viewDogs(request):
    profiles = UserProfile.objects.all()
    context_dict = {'profiles': profiles}
    return render(request, "golden_leash/viewDogs.html", context=context_dict)

def about(request):

	return render(request, "golden_leash/about.html", {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Golden Leash account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, "golden_leash/login.html", {"invalid": True})
    else:
        return render(request, 'golden_leash/login.html', {"invalid": False})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'golden_leash/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)      # means session will be valid and user will therefore not have to log in again
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/golden_leash/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'golden_leash/change_password.html', {
        'form': form
    })

@login_required
def my_account(request):
    return render(request, "golden_leash/my_account.html", {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
