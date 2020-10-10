from django.shortcuts import render, get_object_or_404

from products.models import Product
from .documents import ProductDocument


def search_products(request):
    query = request.GET.get('q')
    results = None
    all_products = list()

    if query:
        results = ProductDocument.search().query(
          "term", title=query
        )

        for elem in list(results):
            temp = get_object_or_404(Product, title=elem.title)
            all_products.append(temp)

    context = {
        'results': results,
        'categorized_products': all_products
    }
    return render(request, 'after_search.html', context)
