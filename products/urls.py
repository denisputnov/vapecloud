from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('cart/', CartTemplate.as_view(), name='cart'),
    url(r'^item/(?P<field_category>[-\w]+)/(?P<field_id>\d+)/$', item_detail, name='goods_detail'),
]