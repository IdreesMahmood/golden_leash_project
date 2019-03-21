import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','golden_leash_project.settings')

import django
django.setup()

from golden_leash.models import UserProfile, Dog
from django.contrib.auth.models import User

    
def populate():
	
	dog_walkers = [{"user": "gav123", "email": "djf2@hot.com", "password":"pass1233", "fullname": "gav m", "address": "dddd", "rating": 5}]
	dog_owners =  [{"user": "alas123","email": "sdqw2@hot.com", "password":"pass1233" , "fullname": "alas i", "address": "mmmm"}]
	dogs = [{"name":"Dave", "age": 9, "breed": "dug", "owner":"dddd"}]
	
	for walker in dog_walkers:
		username = walker["user"]
		email = walker["email"]
		password = walker["password"]
		fullname = walker["fullname"]
		address = walker["address"]
		rating = walker["rating"]
	
		add_walker(username, email, password, fullname, address,rating)
		
	for owner in dog_owners:
		username = owner["user"]
		email = owner["email"]
		password = owner["password"]
		fullname = owner["fullname"]
		address = owner["address"]

		add_owner(username, email, password, fullname, address)
		
	for d in dogs:
		name = d["name"]
		age = d["age"]
		breed = d["breed"]
		owner = d["owner"]
		
		add_dog(name, age, breed, owner)

		
def add_dog(name,age,breed,owner):
	o, bool = UserProfile.objects.get_or_create(address = owner)
	print(o)
	d = Dog.objects.get_or_create(name = name, age = age, breed = breed,  owner = o)[0]
	name = d.name
	age = d.age
	breed = d.breed
	owner = d.owner


def add_user(username, email, password):
	return User.objects.get_or_create(username = username, email = email, password = password)[0]


def add_walker(username, email, password, fullname, address, rating, is_owner = False):
	
	userObject = add_user(username, email, password)

	u = UserProfile.objects.get_or_create(user=userObject, is_owner  = is_owner, fullname = fullname, address = address, rating = rating)[0]
	
	userObject = u.user
	is_owner = u.is_owner
	fullname = u.fullname
	address = u.address
	rating = u.rating
	
	return u


def add_owner(username, email, password, fullname, address, is_owner = True):
	
	userObject = add_user(username, email, password)
	
	u = UserProfile.objects.get_or_create(user=userObject, is_owner  = is_owner, fullname = fullname, address = address)[0]
	
	userObject = u.user
	is_owner = u.is_owner
	fullname = u.fullname
	address = u.address
	
	return u


if __name__ == '__main__':
	print("Starting Golden Leash population script...") 
	populate()