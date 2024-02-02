from django import template

from main.models import Menu

register = template.Library()


@register.inclusion_tag('main/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = Menu.objects.filter(parent=None)
    return {'menu_items': menu_items, 'menu_name': menu_name, 'request': context['request']}
