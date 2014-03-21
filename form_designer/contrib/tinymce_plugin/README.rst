Django Form Designer - TinyMCE plugin
=====================================

This is an optional addon that allows you to use Django Form Designer from
TinyMCE, provided by django-tinymce.

Usage
-----

* Add ``form_designer.contrib.tinymce_plugin`` to your ``INSTALLED_APPS``
  setting.
* In your TinyMCE config add ``formdesigner`` to your ``plugins`` setting and
  also add ``formdesigner`` to your buttons.
* In the template that outputs your model field that tinymce uses you'll need
  to first ``{% load tinymce_formdesigner %}`` and then use the function of
  the same name with your model field:
  ``{% tinymce_formdesigner object.content %}``.

How it works
------------

All the necessary files for the tinymce plugin are served up via static files
when you add the app to your ``INSTALLED_APPS`` setting and they are invoked
by listing ``formdesigner`` in your plugins.

When you click the ``formdesigner`` button on the TinyMCE toolbar it will open
a new popup window that will show you a dialog with a select box containing
all of your form definitions.

When you select and insert a form to your tinymce area what actually gets put
into the content area is an image that has a special class and it's ID is set
to the slug of the form definition. When you use the tinymce_formdesigner tag
on the HTML field it uses BeautifulSoup to parse the HTML content and look for
any images with the special class. When it finds them it replaces the image
with the actual HTML of the form.
