from django.test import TestCase

from products.models import Liquid

if __name__ == '__main__':
    print(Liquid.objects.get(id=1))
