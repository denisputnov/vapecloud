from django_elasticsearch_dsl import Index, Document
from django_elasticsearch_dsl.registries import registry
from products.models import *


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Product
        fields = [
            'title',
            'brand',
            'price',
        ]


@registry.register_document
class LiquidDocument(Document):
    class Index:
        name = 'liquids'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Liquid
        fields = [
            'title',
            'brand',
            'price',
        ]


@registry.register_document
class AccessoryDocument(Document):
    class Index:
        name = 'accessories'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Accessory
        fields = [
            'title',
            'brand',
            'price',
        ]


@registry.register_document
class OthersDocument(Document):
    class Index:
        name = 'others'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Others
        fields = [
            'title',
            'brand',
            'price',
        ]


@registry.register_document
class CloudDocument(Document):
    class Index:
        name = 'clouds'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Cloud
        fields = [
            'title',
            'brand',
            'price',
        ]
# curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d "{\"index.blocks.read_only_allow_delete\": null}"
# curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_cluster/settings -d "{ \"transient\": { \"cluster.routing.allocation.disk.threshold_enabled\": false } }"
# curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
# curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d "{\"transient.cluster.routing.allocation.disk.watermark.low\": \"20gb\",\"transient.cluster.routing.allocation.disk.watermark.high\": \"15gb\",\"transient.cluster.routing.allocation.disk.watermark.flood_stage\": \"10gb\"}"