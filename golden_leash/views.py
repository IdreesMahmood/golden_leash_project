from django.shortcuts import render, redirect
from golden_leash.forms import UserForm, UserProfileForm, UserEditForm, AddDogForm, RemoveDogForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.db.utils import OperationalError
from golden_leash.models import UserProfile, Dog

# Create your views here.

def index(request):
	walker_list = UserProfile.objects.order_by('-rating')[:5]
	try:
		profiles = UserProfile.objects.all()
	except OperationalError:
		pass
	context_dict = {'profiles': profiles, 'ratings': walker_list}
	return render(request, "golden_leash/index.html", context=context_dict)

def walkerProfiles(request):
	try:
		profiles = UserProfile.objects.all()
	except OperationalError:
		pass
	context_dict = {'profiles': profiles}
	return render(request, "golden_leash/walkerProfiles.html", context=context_dict)

def show_walker(request, walker_name_slug):
    context_dict={}
    try:
        profiles = UserProfile.objects.all()
        context_dict = {'profiles': profiles}
    except OperationalError:
        pass


    try:

        walker = UserProfile.objects.get(slug=walker_name_slug)
        if not (walker.is_owner):
            context_dict['walker'] = walker

    except walker.DoesNotExist:
        pass

    return render(request, 'golden_leash/walker.html', context_dict)

def book_dog(request, dog_name_slug):
    context_dict={}
    try:
        profiles = UserProfile.objects.all()
        dogs = Dog.objects.all()
        context_dict = {'profiles': profiles}
    except OperationalError:
        pass

    try:
        dog = Dog.objects.get(slug=dog_name_slug)
        context_dict['dog'] = dog
    except dog.DoesNotExist:
        pass

    if dog:
        dog.available = False
        dog.save()

    return render(request, 'golden_leash/book_dog.html', context_dict)


@login_required
def like_walker(request):
    walker_id = None
    if request.method == 'GET':
        walker_id = request.GET['walker_id']
    likes = 0
    if walker_id:
        walker = UserProfile.objects.get(id=int(walker_id))
        if walker:
            likes = walker.rating + 1
            walker.rating = likes
            walker.save()
    return HttpResponse(likes)

# unused dislike button
# @login_required
# def dislike_walker(request):
#     walker_id = None
#     if request.method == 'GET':
#         walker_id = request.GET['walker_id']
#     likes = 0
#     print("hi")
#     if walker_id:
#         walker = UserProfile.objects.get(id=int(walker_id))
#         if walker:
#             likes = walker.rating - 1
#             walker.rating = likes
#             walker.save()
#     return HttpResponse(likes)

def viewDogs(request):
    try:
        profiles = UserProfile.objects.all()
        dogs = Dog.objects.all()
    except OperationalError:
        pass
    context_dict = {'profiles': profiles, 'dogs': dogs}
    return render(request, "golden_leash/viewDogs.html", context=context_dict)

def about(request):
    try:
        profiles = UserProfile.objects.all()
    except OperationalError:
        pass
    context_dict = {'profiles': profiles}
    return render(request, "golden_leash/about.html", context=context_dict)


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
            profile.is_owner = profile_form.cleaned_data['is_owner']

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],)
            login(request, new_user)
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'golden_leash/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def edit_account(request):
    try:
        profiles = UserProfile.objects.all()
    except OperationalError:
        pass
    context_dict = {'profiles': profiles}
    if request.method == 'POST':
        instanceProfile = None
        for profile in profiles:
            if profile.user == request.user:
                instanceProfile = profile
        form = UserEditForm(data=request.POST, instance=instanceProfile)

        if form.is_valid():
            profile = form.save()
            profile.fullname = form.cleaned_data['fullname']
            profile.address = form.cleaned_data['address']
            profile.picture = form.cleaned_data['picture']
            profile.is_owner = form.cleaned_data['is_owner']
            profile.save()
            return redirect('/golden_leash/my_account/')
    else:
        form = UserEditForm(instance=request.user)
        context_dict['form'] = form
        return render(request, "golden_leash/edit_account.html", context=context_dict)
    return render(request, "golden_leash/edit_account.html", context=context_dict)

@login_required
def add_dog(request):
    form = AddDogForm()

    if request.method == 'POST':
        form = AddDogForm(request.POST)

        if form.is_valid():
            dog = form.save()
            try:
                profiles = UserProfile.objects.all()
            except OperationalError:
                pass
            context_dict = {'profiles': profiles}
            if request.method == 'POST':
                instanceProfile = None
                for profile in profiles:
                    if profile.user == request.user:
                        instanceProfile = profile

            dog.owner = instanceProfile

            form.save(commit=True)

            return redirect('/golden_leash/my_account/')
        else:

            print(form.errors)

    return render(request, 'golden_leash/add_dog.html', {'form': form})

@login_required
def remove_dog(request):
    form = RemoveDogForm()
    if request.method == 'POST':
        form = RemoveDogForm(request.POST)
        if form.is_valid():
            dog_to_remove = None
            try:
                dogs = Dog.objects.all()
            except OperationalError:
                pass
            dog_to_remove_name = form.cleaned_data['name']
            for dog in dogs:
                if dog.name == dog_to_remove_name:
                    dog_to_remove = dog
            try:
                profiles = UserProfile.objects.all()
            except OperationalError:
                pass

            instanceProfile = None
            for profile in profiles:
                if profile.user == request.user:
                    instanceProfile = profile
            if dog_to_remove:
                if dog_to_remove.owner == instanceProfile:
                    dog_to_remove.delete()

            return redirect('/golden_leash/my_account/')
        else:

            return redirect('/golden_leash/my_account/')

    return render(request, 'golden_leash/remove_dog.html', {'form': form})


@login_required
def change_password(request):
    try:
        profiles = UserProfile.objects.all()
    except OperationalError:
        pass
    context_dict = {'profiles': profiles}
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

    context_dict['form'] = form
    return render(request, 'golden_leash/change_password.html', context_dict)

@login_required
def my_account(request):
    try:
        profiles = UserProfile.objects.all()
    except OperationalError:
        pass
    instanceProfile = None
    for profile in profiles:
        if profile.user == request.user:
            instanceProfile = profile
    dogs = Dog.objects.filter(owner=instanceProfile)
    context_dict = {'profiles': profiles, 'dogs': dogs}
    return render(request, "golden_leash/my_account.html", context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
