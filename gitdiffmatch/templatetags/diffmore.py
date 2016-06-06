from django import template

register = template.Library()


def insert(line):
    return line.startswith('-')


def delete(line):
    return line.startswith('+')

register.filter('insert', insert)
register.filter('delete', delete)
