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
    path('logout/',Logout.as_view(),name='logout'),
    path('contact/',ContactView.as_view(),name = 'contact'),
    path('user_dashboard/',UserDashboard.as_view(),name='user_dashboard'),
    path('register/',UserRegister.as_view(),name='register'),
    path('activate/<token>/<uidb64>/',views.activate_account,name='activate'),
    path('basket/',Basket.as_view(),name='basket')
    
]
