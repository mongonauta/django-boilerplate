from fabric.api import local, run
from fabric.colors import blue, red

#######################################################################
#	COMMON TASKS
#######################################################################

def compileMessages () :
	""" PRIVATE: update .MO files """
	local('django-admin.py compilemessages')

def privaterun (env):
	""" PRIVATE: Run server (use <run> command) """
	local ('python manage.py runserver --settings=backend.settings.' + env + '_settings')

def privatetest (env):
	""" PRIVATE: Launch test """
	local ('python manage.py test --settings=backend.settings.' + env + '_settings')

#######################################################################
#	MAIN TASKS
#######################################################################
def install (package) :
	""" Install PIP <package> and update requirements.txt """
	local ('pip install ' + package)
	requirements ()

def clean ():
	""" Cleaning PYC files """
	local ('find . -name "*.pyc" -exec rm -rf {} \;')

def requirements ():
	""" Generate requirements.txt """
	local ('pip freeze > requirements.txt')

def install_requirements():
	""" Install requirements.txt """
	print(green("Installing requirements"))
	local('pip install -r requirements.txt')
	print(green("Installed requirements"))

def createMessages (lang) :
	""" Add new <lang> """
	local ('python manage.py makemessages -l ' + lang)

def collect_static_files():
	""" Collect static files """
	local('python manage.py collectstatic --settings=backend.settings')

def dev () : 
	""" Run server (with locale generation) """
	print(red("Running Dev environment...\n"))
	
	compileMessages ()
	print(blue("\nMO files generated.\n"))

	privaterun('local')
	print(blue("\nServer closed.\n"))

def test () :
	""" Testing apps """
	privatetest ('local')
	print(blue("\nTest passed.\n"))

def commit () :
	pass

def push () :
	pass
	