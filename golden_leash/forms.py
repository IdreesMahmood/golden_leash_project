from django import forms
from django.contrib.auth.models import User
from golden_leash.models import UserProfile, Dog


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'is_owner')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('fullname', 'address', 'picture', 'is_owner')

class AddDogForm(forms.ModelForm):
    nalme = forms.CharField(max_length=128, required=False)
    age = forms.IntegerField(required=False)
    breed = forms.CharField(max_length=128, required=False)
    image = forms.ImageField(required=False)


    class Meta:
        model = Dog
        fields = ('name', 'age', 'breed', 'image')
        exclude = ('owner',)

class RemoveDogForm(forms.ModelForm):
    #name = forms.CharField(max_length=128, required=False)

    class Meta:
        model = Dog
        fields = ('name',)
        exclude = ('owner', 'age', 'breed', 'image',)
class RatingForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ("rating",)        


