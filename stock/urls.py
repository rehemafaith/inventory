from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^brand/$',views.brand,name = 'brand'),
    url('^stores/$',views.stores,name = 'stores'),
    url('^categories/$',views.categories,name = 'categories'),
    url('^product/$',views.product,name = 'product'),
    url('^order/$',views.order,name = 'order'),
]