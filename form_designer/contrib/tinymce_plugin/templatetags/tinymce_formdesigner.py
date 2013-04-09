from django.template.loader import render_to_string
from django.template import RequestContext
from django import template

from BeautifulSoup import BeautifulSoup

from form_designer.models import FormDefinition
from form_designer.views import process_form
from form_designer import settings as app_settings

register = template.Library()

@register.simple_tag(takes_context=True)
def tinymce_formdesigner(context, html):
    """
    This filter expects a chunk of HTML and will look for any <img> tags that
    have a class of tinymce_formdesigner_placeholder, which will be inserted
    by the tinymce plugin. It then replaces those images with the actual form
    output

    This should go before safe in your templates:

        {{ page.content|tinymce_formdesigner|safe }}

    """
    soup = BeautifulSoup(html)
    for tag in soup.findAll("img", { "class": "tinymce_formdesigner_placeholder" }):
        try:
            form_definition = FormDefinition.objects.get(name=tag['id'])
        except FormDefinition.DoesNotExist:
            continue

        if 'request' not in context:
            tag.append(BeautifulSoup('<!-- Failed to render your form. You need to include the request object in the context -->'))
            continue

        result = process_form(context['request'], form_definition,
                              extra_context=RequestContext(context['request']),
                              disable_redirection=True)

        form_template = form_definition.form_template_name or app_settings.DEFAULT_FORM_TEMPLATE

        form_html = BeautifulSoup(render_to_string(form_template, result))

        tag.replaceWith(form_html)

    return str(soup)
