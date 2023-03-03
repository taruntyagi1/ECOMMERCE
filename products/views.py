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
from django.contrib.auth.hashers import make_password
from accounts.utils import send_verification_email
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from accounts.decorator import unauthenticated
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required




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

    @method_decorator(unauthenticated)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request,email = email,password = password)
        if user is not None:
            print("true")
        else:
            print('false')
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



class ContactView(TemplateView):
    template_name = 'contact-v2.html'

    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        return context
    


def handle_404(request,exception):
    return render(request,'404.html')


class UserDashboard(TemplateView):
    template_name = 'user_dashboard.html'


    def post(self,request):
        user_id = request.user.id
        print(request.POST)
       
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        profile = User.objects.filter(id = user_id).update(first_name = first_name,last_name = last_name,username = username,email = email,phone_number = phone_number)
        return redirect('user_dashboard')

   
    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        return context
    

class UserRegister(TemplateView):
    template_name = 'register.html'

    @method_decorator(unauthenticated)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    

    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        profile_photo = request.FILES['image']
        print(request.POST)
        if password != password2:
            messages.error(request,'Password does not match')
        hash_password = make_password(password)
        if User.objects.filter(email = email).exists():
            messages.error(request,"User with this Email already exist")
        if User.objects.filter(username = username).exists():
            messages.error(request,"User with this username is already exists")
        if User.objects.filter(phone_number = phone_number).exists():
            messages.error(request,"User this phone number is already exists")
        user = User.objects.create(first_name = first_name,last_name = last_name,username = username,email = email,phone_number = phone_number,password = hash_password,profile_image = profile_photo)
        
        
        

        user.save()
        send_verification_email(request,user)
        messages.success(request, 'Your account has been created! Please check your email to activate your account.')
        return redirect('home')
    

    def get_context_data(self, **kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        return context
    


def activate_account(request,uidb64,token):
    try:
        uid =  force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = uid)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')



class USerOrders(TemplateView):
    template_name = 'order.html'


    def get_context_data(self,**kwargs):
        context = super(USerOrders,self).get_context_data(**kwargs)
        return context
    

class Basket(TemplateView):
    template_name = 'basket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItems.objects.filter(user=self.request.user)
        print(f"Number of cart items: {len(cart_items)}")
        for item in cart_items:
            print(f"Product: {item.product.title}")
            for variant in item.variant.all():
                print(f"Variant type: {variant.variant_type}")
                print(f"Variant value: {variant.variant_value}")
        context['cart'] = cart_items
        return context

