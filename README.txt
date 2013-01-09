ABOUT
=====

django-snippets enables content managers to maintain small chunks of text
embedded on other pages (i.e., includes out of database).


INSTALLATION
============

python setup.py install

USAGE
=====

As content manager
------------------

Login to the admin site and define snippets of your choice.

Snippets can be deactivated. This will prevent them from being rendered. This
comes handy when you don't need the snippet for the moment but want to keep its
content for later.

As template designer
--------------------

To use a snippet in your templates:

    {% load snippet %}
    
    {# use single- or double-quoted string for hardcoded snippet name #}
    {% get_snippet "home-page-special-message" %}
    {% get_snippet 'welcome' %}
    
    {# or pass a variable #}
    {% get_snippet snippet_variable %}

That's it.

LICENSE
=======

MIT license


AUTHOR
======

Sergiy Kuzmenko
sergiy@kuzmenko.org
