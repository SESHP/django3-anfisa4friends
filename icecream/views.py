from django.shortcuts import render


from .models import icecream_db


def info_ice(request, pk):
    name = icecream_db[pk]['name']
    description = icecream_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/info_ice.html', context)
