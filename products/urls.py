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
    path('user_account/',UserAccount.as_view(),name='user_account'),
    path('register/',UserRegister.as_view(),name='register'),
    path('activate/<token>/<uidb64>/',views.activate_account,name='activate'),
    path('basket/',Basket.as_view(),name='basket'),
    path('filter_name/',FilterName.as_view(),name='filter_name'),
    path('user_address_edit/', UserAddressEdit.as_view(), name='user_address_edit'),
    path('user_orders/',USerOrders.as_view(),name='user_orders'),
    path('user_download/',User_download.as_view(),name='user_download'),
    path('user_address_form/<int:address_id>/',UserAddressForm.as_view(),name='user_address_form'),
    # path('user_address_form/<int:address_id>/',views.address_form,name='user_address_form'),
    path('cart_count/',views.cart_count,name='cart_count'),
    path('payment/',Payment.as_view(),name='payment'),
    path('password_change/',PasswordChange.as_view(),name='password_change'),
    path('user_address_create/',UseraddressCreate.as_view(),name='user_address_create'),
    path('increase/<int:product_id>/',IncreaseQuantity.as_view(),name='increase'),
    path('decrease/<int:product_id>/',DecreaseQuantity.as_view(),name='decrease'),
    path('send_mail/',SendMail.as_view(),name='send_mail'),
    path('search_filter/',views.search_filter,name='search_filter'),
    path('review_create/',Reviews.as_view(),name='review_create'),
    path('session_cart/<int:product_id>/',views.add_to_session_cart,name='session_cart')
   
    
]
