## High level framework written in Python. 
# Used to build complex databse driven websites. 
## Highly structures as lots of strict ways of writing code, but can make this easier to debug too. 

## Django is a web framework. Comes with admin panel, user authentification system, database and ORM (Object Relational Mapper)

## MTV framework
# MODEL deals with data abd databses It can retireve, sotore and change data in a databse. 
# TEMPLATE means how the data look on a website. 
# VIEW means how the data is presented and passes info to the template. 

# SYntax for Django is django-admin<command> [options]

# can start project by typing django-admin startproject projectname 
# it will then create a directory for the project or root folder. 
# manage.py folder within that has specific actions that can be used for the project.

### settings.py is a python file that contains all configurations, which includes installed apps
# will have something like this...
# INSTALLED_APPS = [
#   'django.contrib.admin',
#   'django.contrib.auth',
#   'django.contrib.contenttypes',
#   'django.contrib.sessions',
#   'django.contrib.messages',
#   'django.contrib.staticfiles',
# ]

## and... a database using sqlite3...
# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
#   }
# }

# Also... urls..
# urlpatterns = [
#   path('admin/', admin.site.urls),
# ]

## TO START A SERVER...        python3 manage.py runserver

## python3 manage.py startapp nameofapp   - this creates a new app. 
## then need to add to settings to the list of apps. 
## "nameofapp.apps.nameofappConfig"


