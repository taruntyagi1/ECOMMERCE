from cart.models import *


def get_cart_count(request):
    count = 0
    if request.user.is_authenticated:
        try:
            cart_item = CartItems.objects.filter(user = request.user.id).count()
            if cart_item:
                count = cart_item
            
        except:
            count = 0
    return dict(count=count)


