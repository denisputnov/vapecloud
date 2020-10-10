from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import View, ListView, CreateView

from products.models import *
from search.views import search_products


class BaseView(View):

    def get(self, request):
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
    elif field_category == 'other':
        item = get_object_or_404(Others, slug=field_slug)
    elif field_category == 'cloud':
        item = get_object_or_404(Cloud, slug=field_slug)
    else:
        item = get_object_or_404(Accessory, slug=field_slug)
    return render(request, 'item.html', {'item': item})


class SearchResultsView(ListView):
    model = Product
    template_name = 'search.html'


def get_category(request, field_category):
    if field_category == 'zhidkosti':
        categorized_products = Liquid.objects.all()
    elif field_category == 'other':
        categorized_products = Others.objects.all()
    elif field_category == 'zhidkosti-cloud':
        categorized_products = Cloud.objects.all()
    else:
        categorized_products = list(Accessory.objects.filter(type_category=field_category))
    return render(request, 'categories.html', {'categorized_products': categorized_products})


class SalesTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        saled_products = Product.objects.exclude(sale=0)
        return render(request, 'categories.html', {'categorized_products': saled_products})


class LiquidTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        liguid_products = Liquid.objects.all()

        return render(request, 'categories.html', {'categorized_products': liguid_products})


class AccessoryTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        accessory_products = Accessory.objects.all()
        return render(request, 'categories.html', {'categorized_products': accessory_products})


class OthersTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        accessory_products = Others.objects.all()
        return render(request, 'categories.html', {'categorized_products': accessory_products})


class CloudTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        accessory_products = Cloud.objects.all()
        print(list(accessory_products))
        return render(request, 'categories.html', {'categorized_products': accessory_products})



