from django.urls import path
from products.views  import *
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('shop/',views.shop,name='shop'),
    path('faq/',views.faq,name='faq'),
    path('filter_products/',views.filter_products,name='filter_products'),
    path('single_product/<int:product_id>/',views.single_product_detail,name='single_product'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('login/',LoginView.as_view(),name='login'),
    
]
