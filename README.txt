ABOUT
=====

django-snippets enables content managers to maintain small chunks of text on
various pages on your web site.

One way to tackle this is to simply put appropriate texts into your template.
This however presents a couple challenges. First, you need to re-upload your
template pages each time you want to change that content. Secondly, there is no
easy way to delegate content management of those embedded snippets.
Django-snippets aims to address both of these issues.


INSTALLATION
============

As always: simply put django_snippets on your python search path and add
`snippets` to your list of `INSTALLED_APPS`. Then run syncdb command.


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
