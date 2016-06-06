from django import template

register = template.Library()


def insanddel(line):
    if line.startswith('-'):
        return line
    elif line.startswith('+'):
        return line

register.filter('insanddel', insanddel)
#register.filter('delete', delete)
