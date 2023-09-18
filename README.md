# djangoBlog
# django-admin startproject prjectName is for making project
# python3 manage.py startapp blogName is for making app and we can make several app inside a project
# python3 manage.py runserver is for running the project
# db.sqlite3 will add after running the project

# for more simplicity add new url and add it to project main url.
# make a view and add its url

# add templates for views e.g. home.html, about.html
# from apps in blog app(blog.apps) take the class name e.g. BlogConfig and add it to installed app in settings e.g.'blog.apps.BlogConfig'.
# rendered the home and about pages 
# creating demo date e.g. posts it is list and inside of list there is dictionary
# create some demo date and accessed using context and displayed using for loop in home.html
# def home(request):
#    context = {
#        'posts': posts
#    }
#    return render(request, 'blog/home.html', context)
# used if else for the title {% if %} {% else %} {% endif %}
# reduced the code using parent class


# for accessing to main i have to migrate it (creating database) using python manage.py migrate
# python manage.py createsuperuser
