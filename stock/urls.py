from django.conf.urls import url
from . import views

urlpatterns=[
    
    url('^$',views.product,name = 'product'),
    url('^order/$',views.order,name = 'order'),
    
    url(r'^product/(?P<id>\d+)/delete/$',views.delete_product, name='delete'),
 
]