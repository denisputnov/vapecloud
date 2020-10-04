from django.shortcuts import render, get_object_or_404

from products.models import Product
from .documents import ProductDocument


def search_products(request):
    query = request.GET.get('q')
    results = None
    all_products = list()

    if query:
        results = ProductDocument.search().query(
          "match", title=query
        )

        for elem in list(results):
            temp = get_object_or_404(Product, title=elem.title)
            print(elem)
            all_products.append(temp)

    context = {
        'results': results,
        'list_prod': all_products
    }
    return render(request, 'search.html', context)
