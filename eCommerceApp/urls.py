from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('register/', views.Register, name="register"),
    path('login/', views.User_login, name="login"),
    path('logout/', views.User_logout, name="logout"),
    path('catagery/', views.catagery, name="catagery"),
    path('catagery/products/<str:name>', views.products_type, name="products"),
    path('catagery/products/product_view/<str:pname>/<str:cname>/', views.Product_view, name="product_view"),
    path('catagery/products/product_view/product_detail/<str:id>', views.product_detail, name="products_detail"),
    path('cart/', views.cart, name="cart"),
    path('cart/cart_view', views.Cart_view, name="cart-view"),
    path('cart/cart_remove/<str:cid>', views.cart_remove, name="cart-remove"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('wishlist/wishlist_view', views.wishlist_view, name="wishlist-view"),
    path('wishlist/cart', views.wish_to_cart, name="wish-to-cart"),
    path('wishlist/wishlist_remove/<str:wid>', views.wishlist_remove, name="wishlist_remove"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_DIR)
