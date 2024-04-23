from django.shortcuts import render, redirect
from .form import Register_form, login_form
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    trending = Items.objects.filter(trending = 1)
    context = {'data' : trending}
    return render(request, 'index.html', context)

def Register(request):
    form = Register_form
    context = { 'form' : form }
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        users = User.objects.create_user(username=username, email=email, password=password)
        users.save()
        return redirect('login')
    return render(request, 'register.html',context)

def User_login(request):
    form = login_form
    context = {'form' : form}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully..!!")
            return redirect('/')
        else:
            messages.warning(request, 'invalid users...  Please Register')
            return redirect('login')
    return render(request, 'login.html', context)


def User_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successfully..!!")
    return redirect('login')

# Views
def catagery(request):
    catagery = Catagery.objects.filter(status = 1)
    context = {'catagery' : catagery}
    return render(request, 'products/catagery.html', context)

def products_type(request,name):
    if(Catagery.objects.filter(name =name, status = 1)):
        product = Products.objects.filter(catagery__name = name)
        context = {'product' : product,'catagery_name' : name}
    return render(request, 'products/products.html', context)

def Product_view(request, pname, cname):
    if(Catagery.objects.filter(status = 1)):
        items = Items.objects.filter(products__name = pname)
        context = {'items' : items,"catagery_name" : pname, "product_name":cname}
    return render(request, 'products/product_view.html',context)

def product_detail(request,id):
    detail = Items.objects.filter(id = id)
    context = {"detail" : detail}
    return render(request,'products/product_details.html',context )


def cart(request):
        if request.user.is_authenticated:
            user = request.user
            id= request.GET.get('product_id')
            qty = request.GET.get('product_qty')
            quantity = int(qty)
            product_obj = Items.objects.get(id = id)
            if product_obj:
                if Cart.objects.filter(user = user, product_id = id):
                    messages.warning(request, "Product Already in Cart")
                else:
                    if product_obj.quantity >= quantity:
                        Cart.objects.create(user = user, product = product_obj, product_quantity =quantity)
                        messages.success(request, "Product Added")
            else:
                messages.warning(request,"Out of Stock")
        messages.warning(request,"Please Log In")
        return redirect('cart-view')


def Cart_view(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        context = {'data' : cart}
        return render(request,'products/cart_view.html', context)
    else:
        return redirect('login')



def cart_remove(request, cid):
    remove = Cart.objects.filter(id=cid)
    remove.delete()
    return redirect('cart-view')

def wishlist(request):
        if request.user.is_authenticated:
            user = request.user
            id= request.GET.get('product_id')
            product_obj = Items.objects.get(id = id)
            if product_obj:
                if Wishlist.objects.filter(user = user, items_id = id):
                    messages.warning(request, "Product Already in Favorite")
                else:
                        Wishlist.objects.create(user = user, items = product_obj)
                        messages.success(request, "Product Added")
            else:
                messages.warning(request,"Out of Stock")
        return redirect('wishlist-view')


def wishlist_view(request):
    if request.user.is_authenticated:
        user = request.user
        wislist = Wishlist.objects.filter(user = user)
        context = {'data' : wislist}
        return render(request, 'products/wishlist.html', context)
    

def wish_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        id= request.GET.get('product_id')
        qty = request.GET.get('product_qty')
        product_obj = Items.objects.get(id= id)
        if product_obj:
            if Cart.objects.filter(user = user, product_id = id):
                messages.warning(request, "Product Already in Cart")
            else:
                Cart.objects.create(user = user, product = product_obj, product_quantity = qty)
                messages.success(request, "Product Added")
    messages.warning(request,"Please Log In")
    return redirect('cart-view')


def wishlist_remove(request, wid):
    user = request.user
    print(wid)
    remove = Wishlist.objects.filter(user= user, id=wid)
    remove.delete()
    return redirect('wishlist-view')


