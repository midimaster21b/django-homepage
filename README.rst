=================
 Django Homepage
=================

This is a Django app that displays all the other Django apps that are installed in this instance of Django's project's directory and functions as a fallback splash page when none is specified in the project's urls.py file.

Assumptions
===========

- All apps are located in the project's working path
- Admin is included in your list of installed apps
- All apps have at least an index view defined

Installation
============

.. code-block:: bash

		# Clone the repository to a directory called home in your django working directory.
		git clone git@github.com:midimaster21b/django-home.git DJANGO_PROJECT_DIRECTORY/home

		# Add 'home' to the INSTALLED_APPS variable in the settings.py file.
		emacs DJANGO_PROJECT_DIRECTORY/PROJECT_NAME/settings.py

		# Add home's url to the urls variable in the urls.py file.
		emacs DJANGO_PROJECT_DIRECTORY/PROJECT_NAME/urls.py


**PROJECT_NAME/urls.py**

.. code-block:: python

		urlpatterns = patterns('',
		    ...
		    url(r'^$', include('home.urls')),
		)

**PROJECT_NAME/settings.py**

.. code-block:: python

		INSTALLED_APPS = (
		    ...
		    'home',
		)

Example
-------

.. code-block:: bash

	  git clone git@github.com:midimaster21b/django-home.git /usr/share/django/my_project/home
	  emacs /usr/share/django/my_project/my_project/settings.py
	  emacs /usr/share/django/my_project/my_project/urls.py
