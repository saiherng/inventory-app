
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader


from .models import Item


def index(request):

    items = Item.objects.order_by('id')

    total_price = 0
    for item in items:
        total_price += item.retail_price

    context = {
        'items': items,
        'total_price': str(total_price) + " Kyats"
    }

    return render(request, 'main/index.html', context)


def info(request, item_id):

    try:
        item = Item.objects.get(pk=item_id)

    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    return render(request, 'main/item.html', {'item': item})
