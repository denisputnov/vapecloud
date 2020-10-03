from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Crate)
admin.site.register(Accessory)
admin.site.register(Liquid)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Slider)
admin.site.register(Producted)
admin.site.register(Monitor)
admin.site.register(Desktop)
# admin.site.register(OrderProduct)
# admin.site.register(Order)
# admin.site.register(Cart)
# admin.site.register(CartProduct)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
