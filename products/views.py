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

    data_string = list()

    if field_category == 'zhidkosti':
        categorized_products = Liquid.objects.all()
        for field in Liquid._meta.fields:
            data_string.append(field.name)

    elif field_category == 'other':
        categorized_products = Others.objects.all()
        for field in Others._meta.fields:
            data_string.append(field.name)

    elif field_category == 'zhidkosti-cloud':
        categorized_products = Cloud.objects.all()
        for field in Cloud._meta.fields:
            data_string.append(field.name)

    else:
        categorized_products = list(Accessory.objects.filter(type_category=field_category))
        for field in Accessory._meta.fields:
            data_string.append(field.name)

    return render(request, 'categories.html', {'categorized_products': categorized_products, 'data_string': data_string})


class SalesTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        saled_products = Product.objects.exclude(sale=0)
        data_string = list()
        for field in Product._meta.fields:
            data_string.append(field.name)
        return render(request, 'categories.html', {'categorized_products': saled_products, 'data_string': data_string})


class LiquidTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        liguid_products = Liquid.objects.all()
        data_string = list()
        for field in Liquid._meta.fields:
            data_string.append(field.name)
        return render(request, 'categories.html', {'categorized_products': liguid_products, 'data_string': data_string})


class AccessoryTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        accessory_products = Accessory.objects.all()
        data_string = list()
        for field in Accessory._meta.fields:
            data_string.append(field.name)
        return render(request, 'categories.html', {'categorized_products': accessory_products, 'data_string': data_string})


class OthersTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        accessory_products = Others.objects.all()
        data_string = list()
        for field in Others._meta.fields:
            data_string.append(field.name)
        return render(request, 'categories.html', {'categorized_products': accessory_products, 'data_string': data_string})


class CloudTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        cloud_products = Cloud.objects.all()
        data_string = list()
        for field in Cloud._meta.fields:
            data_string.append(field.name)
        return render(request, 'categories.html', {'categorized_products': cloud_products, 'data_string': data_string})



