from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Crate)
admin.site.register(Accessory)
admin.site.register(Liquid)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartProduct)
