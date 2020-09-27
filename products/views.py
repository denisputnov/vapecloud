from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import View

from products.models import *


class BaseView(View):

    def get(self, request):
        liquids = list(Liquid.objects.all())
        accessories = list(Crate.objects.all())
        products = liquids + accessories
        # for field in products:
        #     print(field.title, int(field.price), field.image)
        return render(request, 'home.html', {'products_list': products})


class ItemTemplate(generic.DetailView):

    def get(self, request, *args, **kwargs):
        return render(request, 'item.html')


class CartTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')


def item_detail(request, field_category, field_id):
    if field_category == 'Жидкости':
        item = get_object_or_404(Liquid, id=field_id)
    else:
        item = get_object_or_404(Crate, id=field_id)
    return render(request, 'item.html', {'item': item})
