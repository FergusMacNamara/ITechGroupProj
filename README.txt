GUGrubGuide      
VERSION 1.0
GUGrubGuide is a web application developed using the Django 1.7  web app framework and Python 2.7.  
The following guidance is on setting up a local instance for test purposes. A population script is included in populate_gugrubguide.py. The included script includes reviews for several restaurants but can be edited as required.

ENVIRONMENT REQUIREMENTS:
Python 2.7 must be installed. Available at https://www.python.org/downloads/
Additionally the packages as listed in “requirements.txt” in the project route directory will need to be installed. These include Django.  This can be achieved using the Setuptools python package available at https://pypi.python.org/pypi/setuptools/1.1.6.
The pip wrapper for SetUptools allows for the quick installation of all required packages. To do so, first issue the command “python ez_setup.py” from the setuptools directory in the command line, followed by “easy_install pip”. 
The command “pip install – r requirements.txt” should then install all further required packages.
SETTING UP :
1, The project folder should be copied to copied to a suitable location. 
2, Via the command line navigate to /ITechGroupProj  and issue the commands:
	python manage.py syncdb
	python manage.py migrate
3, Create a super user account. You will need this to directly manage the database and log on the system without a student email account. (e.g  to add new restaurants or remove inappropriate reviews). To create an account issue the following command and follow the directions on screen:
	python manage.py createsuperuser 
4, Optionally, to populate the database with test data run the population script by issuing the command:
	python populate_gugrubguide.py 
5, To application can be tested locally on a test server by issuing:
	python manage.py runserver <ipaddress>
6, Navigate to <ip address>/gugrubguide   




ACCESS REGISTRATION AND USE:
Viewing Reviews and Restaurant Information:  Once deployed access is available to anyone with a URL. 
Adding Reviews:  To add a review a user will need to first register with the site using an email ending in ”@student.gla.ac.uk”.   (This is limit reviews to those from the perspective of a student). A registration link will be sent to this address.
Adding New Restaurants:  This is currently only available through the administration module provided by Django see below.  You will have to log on to this using a super user account.
ADMINISTRATION AND ADDING RESTAURANTS:
To make changes such as adding a new restaurant or removing a review you will need to use the django admin module at: <local IP address>/admin  and log in with the super user account.  



