from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, Context, loader
from django.http import HttpResponse

from form_designer.models import FormDefinition

def index(request):
    forms = FormDefinition.objects.all().values_list('name', 'title')
    context = {
        'forms': forms,
    }
    return render_to_response('tinymce_plugin/dialog.html',
                              context,
                              context_instance=RequestContext(request))
