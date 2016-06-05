from django.shortcuts import render
from . import utils
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse


def index(request):
    #return HttpResponse("Hello, World. You're at the polls index.")
    diffs = utils.find_diffs("hello1.txt", "hello2.txt")
    template = loader.get_template('gitdiffmatch/index.html')
    context = {
        'diffs': diffs,
    }
    return HttpResponse(template.render(context, request))
