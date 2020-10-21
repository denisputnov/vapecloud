from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import View, ListView, CreateView

from products.models import *
from search.views import search_products


class BaseView(View):

    def get(self, request):
        products = Product.objects.all().filter(new=True).order_by('-add_date','-add_time')
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


def generate_data_string(model):
    result = ''
    all = dict()
    attribute_list = list()
    for elem in model.objects.values():
        result = ''
        temp = ''
        for field in model.objects.values()[0].keys():
            result += f'data-{field}= {elem[field]} '
            temp = f'data-{field}= {elem[field]} '
            all[f'data-{field}'] = elem[field]
        all['attribute'] = temp
        attribute_list.append(result)
    return attribute_list


def get_category(request, field_category):
    if field_category == 'zhidkosti':
        categorized_products = Liquid.objects.all().order_by('add_date','add_time')
        data_list = generate_data_string(Liquid)
        category = 'liquids'

    elif field_category == 'other':
        categorized_products = Others.objects.all().order_by('add_date','add_time')
        data_list = generate_data_string(Others)
        category = 'other'

    elif field_category == 'zhidkosti-cloud':
        categorized_products = Cloud.objects.all().order_by('add_date','add_time')
        data_list = generate_data_string(Cloud)
        category = 'liquids'

    else:
        categorized_products = list(Accessory.objects.filter(type_category=field_category))
        data_list = generate_data_string(Accessory)
        category = 'accessory'

    return render(request, 'categories.html', {'categorized_products': categorized_products, 'data_string': data_list, 'category': category})


class SalesTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        saled_products = Product.objects.exclude(sale=0).order_by('add_date','add_time')
        data_list = generate_data_string(Product)

        category = 'sales'

        return render(request, 'categories.html',
                      {'categorized_products': saled_products, 'data_string': data_list, 'category': category})


class LiquidTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        liquid_products = Liquid.objects.all().order_by('add_date','add_time')
        data_list = generate_data_string(Liquid)

        category = 'liquids'

        return render(request, 'categories.html',
                      {'categorized_products': liquid_products, 'data_string': data_list, 'category': category})


class AccessoryTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        accessory_products = Accessory.objects.all().order_by('add_date','add_time')
        data_list = generate_data_string(Accessory)

        category = 'accessory'

        return render(request, 'categories.html',
                      {'categorized_products': accessory_products, 'data_string': data_list, 'category': category})


class OthersTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        other_products = Others.objects.all().order_by('add_date','add_time')
        data_list = generate_data_string(Others)
        category = 'other'
        return render(request, 'categories.html',
                      {'categorized_products': other_products, 'data_string': data_list, 'category': category})


class CloudTemplate(BaseView):

    def get(self, request, *args, **kwargs):
        cloud_products = Cloud.objects.all().order_by('add_date','add_time')
        data_list = generate_data_string(Cloud)
        category = 'cloud'
        return render(request, 'categories.html',
                      {'categorized_products': cloud_products, 'data_string': data_list, 'category': category})
