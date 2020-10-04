from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import View, ListView

from products.models import *


class BaseView(View):

    def get(self, request):
        liquids = list(Liquid.objects.all().filter(new=True))
        accessories = list(Accessory.objects.all().filter(new=True))
        # products = liquids + accessories
        products = Product.objects.all().filter(new=True)
        slider = list(Slider.objects.all())
        return render(request, 'home.html', {'products_list': products, 'slider_list': slider})


class ItemTemplate(generic.DetailView):

    def get(self, request, *args, **kwargs):
        return render(request, 'item.html')


class CartTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')


def item_detail(request, field_category, field_slug):
    if field_category == 'zhidkosti':
        item = get_object_or_404(Liquid, slug=field_slug)
    else:
        item = get_object_or_404(Accessory, slug=field_slug)
    return render(request, 'item.html', {'item': item})


class SearchResultsView(ListView):
    model = Product
    template_name = 'search.html'



class TEST(generic.DetailView):

    def get(self, request, *args, **kwargs):
        return render(request, 'after_search.html')
