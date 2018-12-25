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

##### 



##### Developer Notes

- Django will be available only when the environment is active.

directory learning_log
    source 11_env/bin/activate
    python manage.py runserver
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

- End on p. 412


18-2. Short Entries: The __str__() method in the Entry model currently appends
an ellipsis to every instance of Entry when Django shows it in the admin site 
or the shell. Add an if statement to the __str__() method that adds an
ellipsis only if the entry is more than 50 characters long . Use the admin
site to add an entry that’s fewer than 50 characters in length, and check that
it doesn’t have an ellipsis when viewed.






