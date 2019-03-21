from django.test import TestCase
from django.contrib.staticfiles import finders
from django.core.urlresolvers import reverse
from golden_leash.forms import UserForm, UserEditForm, RatingForm
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomepageTests(TestCase):

    # tests that the homepage uses template
    def test_homepage_uses_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'golden_leash/index.html')


    # checks to see that the hompage has a title
    def test_homepage_has_title(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutpageTests(TestCase):

    # tests that the about page uses template
    def test_about_uses_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'golden_leash/about.html')


    #tests to see if the about page displays the admin contact details
    def test_does_about_contain_contact_details(self):
        response = self.client.get(reverse('about'))                      
        self.assertIn(b'Alastair Innes', response.content)



class StaticImageTests(TestCase):

    #checks if static media is being used properly
    def test_correct_static_images(self):
        image = finders.find('images/dog.jpg')
        self.assertIsNotNone(image)
 
class UserFormTests(TestCase):

    #tests if the user form is valid when given valid data
    def test_user_form_valid(self):
        form = UserForm(data={'username': "user123", 'email': "a@b.com", 'password': "password123"})
        self.assertTrue(form.is_valid())


    #tests if the user form is valid when given invalid data
    def test_user_form_invalid(self):
        form = UserForm(data={'username': "user123", 'email': "a@b.com", 'number': "5687"})
        self.assertFalse(form.is_valid())

class UserEditFormTests(TestCase):

    #tests if the eser edit form is valid when given valid data
    def test_user_edit_form_valid(self):
        form = UserEditForm(data={'fullname': "Ben", 'address': "aaaaa", 'picture': 'dog.jpg', 'is_owner': True})
        self.assertTrue(form.is_valid())


    #tests if the eser edit form is invalid when given invalid data
    def test_user_edit_form_invalid(self):
        form = UserEditForm(data={'name': 15})
        self.assertFalse(form.is_valid())

class RatingFormTests(TestCase):

    #tests if the ratings form is valid when given valid data
    def test_rating_form_valid(self):
        form = RatingForm(data={'rating': 3})
        self.assertTrue(form.is_valid())


    #tests if the ratings form is invalid when given invalid data
    def test_rating_form_invalid(self):
        form = RatingForm(data={'number': 35})
        self.assertFalse(form.is_valid())



    
