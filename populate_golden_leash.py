import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','golden_leash_project.settings')

import django
django.setup()

from golden_leash.models import UserProfile, Dog
from django.contrib.auth.models import User

    
def populate():
	
	# add default data for the population
	dog_walkers = [{"user": "gav123", "email": "gav99@hotmail.com", "password":"pass1233", "fullname": "Gavin Mooney", "address": "EK", "rating": 2},
		{"user": "john12", "email": "john@hotmail.com", "password":"xx99123s", "fullname": "John Stones", "address": "4 Park Lane", "rating": 205},
		{"user": "lucy98", "email": "lucy33@hotmail.com", "password":"red99a", "fullname": "Lucy Mclean", "address": "43 Davidson Court", "rating": 78},
		{"user": "idrees", "email": "Id99@gmail.com", "password":"QWERTY00", "fullname": "Idrees Mahmood", "address": "109 Preston Lane", "rating": 108}]
	
	dog_owners =  [{"user": "alas123","email": "bigALAS@celtic.co.uk", "password":"pass3456" , "fullname": "Alastair Innes", "address": "Celtic Park"},
		{"user": "Jamie999","email": "jamie@gmail.com", "password":"js12345" , "fullname": "Jamie Sinclair", "address": "45 Glasgow Road"}]
	
	dogs = [{"name":"Dave", "age": 9, "breed": "dug", "owner":"Celtic Park"},
		{"name":"Benji", "age": 2, "breed": "Labrador", "owner":"Celtic Park"},
		{"name":"Rex", "age": 4, "breed": "Cocker Spaniel", "owner":"45 Glasgow Road"}]
	
	# add walkers from list
	for walker in dog_walkers:
		username = walker["user"]
		email = walker["email"]
		password = walker["password"]
		fullname = walker["fullname"]
		address = walker["address"]
		rating = walker["rating"]
	
		add_walker(username, email, password, fullname, address,rating)
	
	# add owners from list 
	for owner in dog_owners:
		username = owner["user"]
		email = owner["email"]
		password = owner["password"]
		fullname = owner["fullname"]
		address = owner["address"]

		add_owner(username, email, password, fullname, address)
	
	# add dogs from list 	
	for d in dogs:
		name = d["name"]
		age = d["age"]
		breed = d["breed"]
		owner = d["owner"]
		
		add_dog(name, age, breed, owner)

# create new dog model		
def add_dog(name,age,breed,owner):
	o, bool = UserProfile.objects.get_or_create(address = owner)
	
	d = Dog.objects.get_or_create(name = name, age = age, breed = breed,  owner = o)[0]
	name = d.name
	age = d.age
	breed = d.breed
	owner = d.owner

# returns a user that can be used to populate userObject
def add_user(username, email, password):
	return User.objects.get_or_create(username = username, email = email, password = password)[0]

#create new walker model
def add_walker(username, email, password, fullname, address, rating, is_owner = False):
	
	userObject = add_user(username, email, password)

	u = UserProfile.objects.get_or_create(user=userObject, is_owner  = is_owner, fullname = fullname, address = address, rating = rating)[0]
	
	userObject = u.user
	is_owner = u.is_owner
	fullname = u.fullname
	address = u.address
	rating = u.rating
	
	return u

# create new owner model
def add_owner(username, email, password, fullname, address, is_owner = True):
	
	userObject = add_user(username, email, password)
	
	u = UserProfile.objects.get_or_create(user=userObject, is_owner  = is_owner, fullname = fullname, address = address)[0]
	
	userObject = u.user
	is_owner = u.is_owner
	fullname = u.fullname
	address = u.address
	
	return u

# run script 
if __name__ == '__main__':
	print("Starting Golden Leash population script...") 
	populate()