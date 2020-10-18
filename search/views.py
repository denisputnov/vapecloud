from django.shortcuts import render, get_object_or_404

from products.models import *
from .documents import *


def get_object_or_none(klass, *args, **kwargs):
    try:
        return klass._default_manager.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None


def search_products(request):
    query = request.GET.get('q').lower()
    results = None
    all_products = list()

    if query:
        # results = list(ProductDocument.search().query(
        #   "term", title=query
        # ))
        # python manage.py search_index --rebuild  curl -XPUT localhost:9200/_settings?pretty -H 'Content-Type: products/json' -d "index.blocks.read_only_allow_delete": null
        # curl -XPUT localhost:9200/_settings?pretty -H 'Content-Type: products/json' -d "index.blocks.read_only_allow_delete": null
        # curl -XPUT -H "Content-Type: application/json" localhost:9200/_all/_settings -d {"index.blocks.read_only_allow_delete": null}
        results = list(LiquidDocument.search().query(
            "term", title=query
        ))
        results += list(AccessoryDocument.search().query(
            "term", title=query
        ))
        results += list(CloudDocument.search().query(
            "term", title=query
        ))
        results += list(OthersDocument.search().query(
            "term", title=query
        ))

        for elem in list(results):
            temp = get_object_or_404(Product, title=elem.title)
            all_products.append(temp)
            # query_sets = []  # Общий QuerySet
            #
            # all_products.append(get_object_or_none(Cloud, title=elem.title))
            # all_products.append(get_object_or_none(Liquid, title=elem.title))
            # all_products.append(get_object_or_none(Accessory, title=elem.title))
            # all_products.append(get_object_or_none(Others, title=elem.title))
            # Ищем по всем моделям
            # all_products.append(Liquid.objects.get(title=elem.title))
            # all_products.append(Accessory.objects.get(title=elem.title))
            # all_products.append(Cloud.objects.get(title=elem.title))
            # all_products.append(Others.objects.get(title=elem.title))

    context = {
        'results': results,
        'categorized_products': all_products
    }
    return render(request, 'after_search.html', context)
