from django.shortcuts import render


def index(request):
    return render(request, 'main/base.html')


def show_menu(request, menu_slug):
    return render(request, 'main/menu.html', {'menu_name': menu_slug})
