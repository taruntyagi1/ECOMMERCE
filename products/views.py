from django.shortcuts import render,redirect
from products.models import *
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from category.models import *
from accounts.models import User
from cart.models import *
from django.views.generic import TemplateView,ListView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View



def home(request):
    products = Product.objects.all().order_by('id')[:8]
    new_product = Product.objects.filter(is_active =  True).order_by('created_at')[:4]
    
    context = {
        'products' : products,
        'new_product' : new_product
        
    }
    return render(request,'index.html',context)





def faq(request):
    return render(request,'faqs.html')


def shop(request):
    product_list = Product.objects.all().order_by('id')
    paginator = Paginator(product_list, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
   

    context = {
        'products' : products,
        
    }
    return render(request, 'shop-3col-slide.html',context)



def filter_products(request):
    category_slug = request.GET.get('category')
    category = Category.objects.get(slug = category_slug)
    products = Product.objects.filter(category=category)

    context = {
        
        'products': products,
    }

    return render(request,'shop-3col-slide.html',context)



def single_product_detail(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    image = Product_images.objects.filter(product = product,is_active = True)
    variant = Variant.objects.filter(product = product)
   
    context = {
        'product' : product,
        'image' : image,
        'variant' : variant,
        
    }

    return render(request,'shop-detail-des.html',context)

def add_to_cart(request, product_id):
    if request.method == "POST":
        print(request.POST)
        product = Product.objects.get(id=product_id)
        user = User.objects.get(id=request.user.id)

        product_variant = []
        for items in request.POST:
            key = items
            value = request.POST[key]

            try:
                variant = Variant.objects.get(variant_type=key, variant_value=value)
                print(variant)
                product_variant.append(variant)
            except:
                pass

        cart, created = Cart.objects.get_or_create(user=user, is_paid=False)
        cart_item = None
        # Check if a cart item already exists with the same product and variants
        existing_cart_items = CartItems.objects.filter(
            user=user,
            cart=cart,
            product=product,
        )
        for item in existing_cart_items:
            if set(item.variant.all()) == set(product_variant):
                cart_item = item
                break

        if cart_item is None:
            # If no cart item exists, create a new one
            cart_item = CartItems.objects.create(
                user=user,
                cart=cart,
                product=product,
                quantity=1,
                price=product.min_price,
            )
            for item in product_variant:
                cart_item.variant.add(item)
        else:
            # If a cart item already exists, update its quantity and price
            cart_item.quantity += 1
            cart_item.price = cart_item.product.min_price * cart_item.quantity
            cart_item.save()

        return redirect('home')


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request,email = email,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'you are logged in')
            return redirect('home')
        else:
            messages.error(request,'Validation error')
            return redirect('login')
        


    def get_context_data(self,*args,**kwargs):
        context = super(self.__class__,self).get_context_data(*args,**kwargs)
        
        return context



class Logout(View):

    def get(self,request):
        logout(request)
        return redirect('home')
