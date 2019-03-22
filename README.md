# golden_leash_project
The golden leash is a project that enable dog walkers to communicate with dog owners to book appointments 
with them to walk their dogs. Owners are able to upload what dogs they want to be walked and can "upvote" each
walker if they are satisfied with their service. Walkers are able to view each dog and can book to walk them through email.

To run on your own machine, you must have a Python 3.7 virtual enviornment with Django 1.11.17 and Pillow installed.
Before running the server, you must write "pip install -r requirements.txt" into the command line, then 
"python manage.py makemigrations golden_leash" and "python manage.py migrate". to populte the database, enter "python populate_golden_leash.py" into the command prompt To run the server, use "python manage.py runserver" and put the URL displayed in the command prompt into a web browser.

To run the tests, type "python golden_leash/tests.py" into the command prompt. This will perform the unit testing
of the project.

Live deployment of project - http://gavjmooney.pythonanywhere.com/

External APIs:
Google Maps API
Bootstrap
JQuery

Authors:
Alastair Innes
Idrees Mahmood
Gavin Mooney
Jamie Sinclair
