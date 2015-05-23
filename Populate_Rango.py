import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_cat = add_cat('Python')
    add_page(cat=python_cat, title = "How to Think like a Computer Scientist", url = "http://www.greenteapress.com/thinkpython/")

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url = url, views = views)[0]
    p.save()
    return p

if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()