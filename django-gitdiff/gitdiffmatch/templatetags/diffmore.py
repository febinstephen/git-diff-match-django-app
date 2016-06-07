from django import template

register = template.Library()


def insert(line):
        if line.startswith('+'):
            return line
        else:
            return '-----------'


def delete(line):
        if line.startswith('-'):
            return line
        else:
            return '------------'


register.filter('insert', insert)
register.filter('delete', delete)
