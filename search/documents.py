from django_elasticsearch_dsl import Index, Document
from django_elasticsearch_dsl.registries import registry
from products.models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {'number_of_shards' :1, 'number_of_replicas' : 1}

    class Django:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
        ]
