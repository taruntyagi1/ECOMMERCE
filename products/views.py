from django.shortcuts import render,redirect,HttpResponse
from products.models import *
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from category.models import *
from accounts.models import User,UserAddress
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
from django.contrib.auth.decorators import login_required,user_passes_test
from orders.models import*
from django.urls import reverse_lazy
from cart.context_processor import get_cart_count

    
    
        


def home(request):
    products = Product.objects.all().order_by('id')[:8]
    new_product = Product.objects.filter(is_active =  True).order_by('created_at')[:4]
    
    context = {
        'products' : products,
        'new_product' : new_product
        
    }
    return render(request,'index.html',context)


class Homepage(TemplateView):

    template_name = 'index.html'
    def  get_context_data(self,*args,**kwargs):
        context = super(self.__class__,self).get_context_data(*args,**kwargs)
        return context
    
# class SingleProduct(TemplateView):
#     template_name = 'shop-details-des.html'

#     def get_context_data(self,*args,**kwargs):
#         context = super(self.__class__,self).get_context_data(**kwargs)
#         product = Product.objects.get(id = kwargs['product_id'])
#         image = Product_images.objects.filter(product = product,is_active = True)
#         variant = Variant.objects.filter(product = product)
#         context 


def faq(request):
    return render(request,'faqs.html')




    


def shop(request):
    products = Product.objects.all().order_by('id')
    
   

    context = {
        'products' : products,
        
    }
    return render(request, 'shop-5col.html',context)



def filter_products(request):
    category_slug = request.GET.get('category')
    category = Category.objects.get(slug = category_slug)
    products = Product.objects.filter(category=category)

    context = {
        
        'products': products,
    }

    return render(request,'shop-5col.html',context)


class FilterName(View):

    def post(self,request):
        print(request.POST)
        cat_name = request.POST.get('cat_name')
        # category = Category.objects.get(title = cat_name)
        products = Product.objects.filter(description__icontains=cat_name)

        context = {
            'products' : products,
            
        }

        return render(request,'shop-5col.html',context)
    



    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        return context



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
            except Variant.DoesNotExist:
                variant = None

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


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator

class LoginView(TemplateView):
    template_name = 'login.html'

    @method_decorator(require_http_methods(["GET", "POST"]))
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        self.next_url = request.GET.get('next')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in.')
            if self.next_url:
                return redirect(self.next_url)
            else:
                return redirect('home')
        else:
            messages.error(request, 'Validation error.')
            return redirect('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['next'] = self.next_url
        return context


class Login_for_requested_path(TemplateView):
    template_name = 'login.html'
    


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)

        return render(request, self.template_name)
    

    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email = email,password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect(self.get_success_url())

        messages.error(request, 'Invalid email or password')
        return redirect('login')
    
    def get_success_url(self):
        redirect_to = self.request.GET.get('next', '')
        if redirect_to:
            return redirect_to
        else:
            return self.success_url



    


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


class UserAccount(TemplateView):
    template_name = 'user_account.html'


    def post(self,request):
        user_id = request.user.id
        print(request.POST)
       
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        profile = User.objects.filter(id = user_id).update(first_name = first_name,last_name = last_name,username = username,email = email,phone_number = phone_number)
        return redirect('user_account')

   
    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        # context['user'] = User.objects.filter(id = self.request.user.id)
        
       
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
    template_name = 'orders.html'

    @method_decorator(login_required(login_url='request_path_login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,**kwargs):
        context = super(USerOrders,self).get_context_data(**kwargs)
        orders = Orders.objects.filter(user = self.request.user)
        context['orders'] = orders
        
        return context
  
class User_download(TemplateView):
    template_name = 'downloads.html'


    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

   
    def get_context_data(self,**kwargs):
        context = super(User_download,self).get_context_data(**kwargs)
        order = Orders.objects.filter(user = self.request.user)
        context['order'] = order
        return context
    

    

class Basket(TemplateView):
    template_name = 'basket.html'


    def post(self, request):
        code = request.POST.get('voucher_code')
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        cart = Cart.objects.get(user=user)
        cart_items = CartItems.objects.get(user=user, cart=cart)

        try:
            voucher = Voucher.objects.get(voucher_code=code)
            print(voucher)
        except Voucher.DoesNotExist:
            messages.error(request, 'voucher does not exist')
            return redirect('basket')

        
        if int(cart_items.get_cart_total()) < voucher.min_value:
                messages.error(request, f"Minimum spend is {voucher.min_value} ")

                return redirect('basket')

        if voucher.discount_type == 'Fixed':
            
            cart_items.price = max(cart_items.price - voucher.discount_value, 0)
            cart_items.save()
            voucher.is_active = False
            voucher.save()

        if voucher.discount_type == 'Percentage':
            cart_items.price = max(cart_items.price - voucher.discount_value,0)
            cart_items.save()

        return redirect('basket')

            


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        cart_items = CartItems.objects.filter(user=self.request.user.id)
        cart_item_price= 0
        for items in cart_items:
        
            cart_item_price = items.get_cart_total()
        # print(f"Number of cart items: {len(cart_items)}")
        # for item in cart_items:
        #     print(f"Product: {item.product.title}")
        #     for variant in item.variant.all():
        #         print(f"Variant type: {variant.variant_type}")
        #         print(f"Variant value: {variant.variant_value}")
        context['cart'] = cart_items
        context ['total_price'] = cart_item_price
        
        return context




    
class PasswordChange(View):


    def post(self,request):
        current_password = request.POST.get('current_password')
        if current_password !=self.request.user.password:
            messages.error(request,"Current password not match")
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 !=password2:
            messages.error(request,"Password does not match")
        password = make_password(password1)
        user = User.objects.filter(id = self.request.user.id).update(password =password)
        if user:
            messages.success(request,'Password change successfully')

class UseraddressCreate(View):

    def post(self,request):
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        address_type = request.POST.get("address_type")
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zipcode = request.POST.get('zipcode')

        user_address = UserAddress.objects.create(user = self.request.user,address1 = address1,address2 = address2,city = city,state = state,country = country,pin_code = zipcode,address_type = address_type)
        user_address.save()
        messages.success(request,'Address save successfully')


# def address_form(request,address_id):
#     address = get_object_or_404(UserAddress,id = address_id)
#     context = {
#         'address' : address
#     }
#     return render(request,'user_address_form.html',context)
    
    # def post(self,request):
    #     address_id = request.POST.get('address_id')
        
    #     address = UserAddress.objects.filter(id = address_id,user = self.request.user).first()
    #     if address:
    #         address.address1 = request.POST.get('address1',address.address1)
    #         address.address2 = request.POST.get('address2', address.address2)
    #         address.address_type = request.POST.get('address_type', address.address_type)
    #         address.country = request.POST.get('country', address.country)
    #         address.state = request.POST.get('state', address.state)
    #         address.city = request.POST.get('city', address.city)
    #         address.pin_code = request.POST.get('zip_code', address.pin_code)
    #         address.save()
    #         messages.success(request,'Address chnage successfully')

    #     else:
    #         messages.error(request, 'Address not found.')

class UserAddressForm(TemplateView):
    template_name = 'user_address_form.html'

    def get_context_data(self,address_id,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        context['address'] = get_object_or_404(UserAddress,id = address_id)
        return context

class UserAddressEdit(TemplateView):

    template_name = 'user_address.html'

    
    def get_context_data(self,**kwargs):
        context = super(UserAddressEdit,self).get_context_data(**kwargs)
        address = UserAddress.objects.filter(user = self.request.user)
        context['address'] = address
        return context

    def post(self,request):
        address_id = request.POST.get('address_id')
        
        
        address = UserAddress.objects.filter(id = address_id,user = self.request.user).first()
        if address:
            print(request.POST)
            address.address1 = request.POST.get('address1',address.address1)
            address.address2 = request.POST.get('address2', address.address2)
            address.address_type = request.POST.get('address_type', address.address_type)
            address.country = request.POST.get('country', address.country)
            address.state = request.POST.get('state', address.state)
            address.city = request.POST.get('city', address.city)
            address.pin_code = request.POST.get('pin_code', address.pin_code)
            address.save()
            messages.success(request,'Address chnage successfully')
            return redirect('user_address_edit')
        else:
            messages.error(request,'Address not save')

        # else:
        #     messages.error(request, 'Address not found.')
        #     return redirect('user_address_form')
            


        
class Checkout(TemplateView):
    template_name = 'payment.html'

    def psot(self,request):
        user_id = self.request.user.id
        user = User.objects.get(id = user_id)
        cart = Cart.objects.get(user = user)
        cart_item = CartItems.objects.get(cart = cart,user = user)
        order = Orders.objects.get(user = user)
        

    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        return context
    

class IncreaseQuantity(View):

    def get(self,request):
        user_id = self.request.user.id
        user = User.objects.get(id = user_id)
        cart = Cart.objects.get(user = user)
        cart_item = CartItems.objects.get(cart = cart,user = user)
        cart_item.quantity +=1
        cart_item.price = cart_item.quantity *cart_item.product.min_price
        cart_item.save()
        messages.success(request,'Quantity increases')
        return redirect('basket')
    
class DecreaseQuantity(View):

    def get(self,request):

        user_id = self.request.user.id
        user = User.objects.get(id = user_id)
        cart = Cart.objects.get(user = user)
        cart_item = CartItems.objects.get(cart = cart,user = user)
        try:
            cart_item.quantity -= 1
            cart_item.price = cart_item.price - cart_item.product.min_price
            if cart_item.quantity <=0:
                cart_item.delete()
                return redirect('basket')
            cart_item.save()
            
            messages.success(request,'Quantity Decrease')
            return redirect('basket')
        except CartItems.DoesNotExist:
            messages.error(request,"Cart item not found")
        return redirect('basket')
