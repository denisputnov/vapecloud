from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('cart/', CartTemplate.as_view(), name='cart'),
    url(r'^item/(?P<field_category>[-\w]+)/(?P<field_slug>[-\w]+)/$', item_detail, name='goods_detail'),
    # path('test/', get_category, name='test'),
    path('accessories/', AccessoryTemplate.as_view(), name='cart'),
    path('zhidkosti/', LiquidTemplate.as_view(), name='cart'),
    path('sales/', SalesTemplate.as_view(), name='cart'),
    path('cloud/', CloudTemplate.as_view(), name='cart'),
    path('other/', OthersTemplate.as_view(), name='cart'),
    url(r'^accessories/(?P<field_category>[-\w]+)/$', get_category, name='goods_detail'),
    url(r'^cloud/(?P<field_category>[-\w]+)/$', get_category, name='goods_detail'),
]
