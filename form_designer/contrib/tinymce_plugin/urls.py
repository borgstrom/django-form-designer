from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'form_designer.contrib.tinymce_plugin.views',

    url(r'^$', 'index', name='tinymce_plugin'),
)
