from django.conf.urls import url
from . import views
import notifications.urls

urlpatterns=[
  
    url('^$',views.product,name = 'product'),
    url('^order/$',views.order,name = 'order'),
    url('^reorder/$',views.reorder,name = 'reorder'),
    url(r'^(?P<id>\d+)/delete/$',views.delete_product, name='delete'),
    url(r'^(?P<id>\d+)/edit/$', views.editproduct, name='editproduct'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]