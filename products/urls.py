from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('cart/', CartTemplate.as_view(), name='cart'),
    url(r'^item/(?P<field_category>[-\w]+)/(?P<field_slug>[-\w]+)/$', item_detail, name='goods_detail'),
    path('test/', TEST.as_view(), name='test'),
    path('accessories/', TEST.as_view(), name='cart'),
    path('zhidkosti/', TEST.as_view(), name='cart'),
    path('sales/', TEST.as_view(), name='cart'),
    path('cloud/', TEST.as_view(), name='cart'),
    path('other/', TEST.as_view(), name='cart'),
    url(r'^accessories/(?P<field_category>[-\w]+)/$', TEST.as_view(), name='goods_detail'),
    url(r'^cloud/(?P<field_category>[-\w]+)/$', TEST.as_view(), name='goods_detail'),
]
