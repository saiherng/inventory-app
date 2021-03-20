from django.shortcuts import render

from django.http import HttpResponse

from .models import Item
from django.template import loader


def index(request):
    items = Item.objects.order_by('id')
    context = {'items': items}

    return render(request, 'main/index.html', context)
