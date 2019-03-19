from django.shortcuts import render
from golden_leash.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def index(request):

    return render(request, "golden_leash/index.html", {})

def walkerProfiles(request):

	return render(request, "golden_leash/walkerProfiles.html", {})

def viewDogs(request):

	return render(request, "golden_leash/viewDogs.html", {})

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

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
