from django.shortcuts import render
from . import utils
from django.http import HttpResponse
from django.template import loader


def index(request):
    diffs = utils.finddiffs_of_two_files("hello1.txt", "hello2.txt").split('\n')
    #diffs = utils.finddiffs_of_two_strings("i am not dump", "i was not hero").split('\n')
    template = loader.get_template('gitdiffmatch/index.html')
    context = {
        'diff': diffs,
    }
    return HttpResponse(template.render(context, request))
