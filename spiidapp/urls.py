from django.urls import path
from .import views

urlpatterns = [
    path('base/',views.base, name='base'),
    path('',views.home, name='home'),
    path('checkout/',views.checkout, name='checkout'),
    path('product/<int:id>',views.product, name='product'),
    path('cart/',views.cart, name='cart'),
    path('store/', views.store, name="store"),
	path('update_item/', views.updateItem, name="update_item"),
]
