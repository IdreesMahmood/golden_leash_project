from django.test import TestCase
from django.contrib.staticfiles import finders
from django.core.urlresolvers import reverse


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
    def test_homepage_uses_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'golden_leash/about.html')

    #tests to see if the about page displays the admin contact details
    def test_does_about_contain_contact_details(self):
        # Check if the index page contains an img
        response = self.client.get(reverse('about'))
        self.assertIn(b'Alastair Innes', response.content)



class StaticFilesTests(TestCase):

    #checks if static media is being used properly
    def test_serving_static_files(self):
        result = finders.find('images/dog.jpg')
        self.assertIsNotNone(result)
