# Webapps

### Getting Started With Django

http://djangoproject.com/

##### Project Spec

I will write a web app called Learning Log that allows me to log the
topics I'm interested in and to make journal entries as I learn
about each topic.

The Learning Log home page should describe the site
and invite other users to either register or log in.

Once logged in, a user should be able to create new topics,
add new entries, and read and edit existing entries.


##### Developer Notes

- Django will be available only when the environment is active.

directory learning_log
    `source 11_env/bin/activate`
    `python manage.py runserver`
        (the focus here is to run the manage.py file)

directory learning_logs
    git root folder

- Book states the following: 
    If you’re using Python 2.7, you should call the
    __str__() method__unicode__() instead. The body of the
    method is identical.
    
- In REALITY, python 2.7 can take the __str__() method and return
the properly given string.

- Django APIs
    https://docs.djangoproject.com/en/2.1/ref/

- Django 2.0 removes the `django.core.urlresolvers` module, which was
moved to django.urls in version 1.10. Change any import to use
django.urls instead, like this: `django.urls import reverse`
https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers

##### Django Templates Documentation
    * https://docs.djangoproject.com/en/2.1/topics/templates/


##### Python Manage Shell 
1. Activate virtual environment.
2. python manage.py shell
3. (11_env) Kenneths-MacBook-Pro:learning_log everydaykenneth$ python manage.py shell
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: 11_admin>]>
>>> for user in User.objects.all():
...     print(user.username, user.id)
... 
11_admin 1
>>> 

# End at Restricting Topics Access to Appropriate Users


