django-uuidfield
====================

There are a few UUID fields floating around out on the interwebs.

Here is one packaged up as a pip installable one. It is mostly based on
http://gist.github.com/374662, but has some changes, and will get some
unit tests.

Installation
--------------

Download or clone the repository, and from inside the root folder::

  $ python setup.py install
  
Or, use pip::

  $ pip install -e hg+https://bitbucket.org/schinckel/django-uuidfield#egg=django-uuidfield

Even better, do this from inside your virtualenv.

You are using virtualenv, right?


Django setup
--------------

You don't really need to install into your INSTALLED_APPS, but you may
want to. I generally put everything in there that I use, just so any tests
on it will be run when you test your project.

Then, in your model file::

    from django.db import models
    import uuidfield
  
    class MyModel(models.Model):
        uuid = uuidfield.UUIDField()

Advanced use
--------------

The following arguments can be passed to the UUIDField:
  
  * ``auto`` - a boolean value as to if values should be generated
    automatically.