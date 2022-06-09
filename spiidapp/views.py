from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator




#Views
def base(request):
    return render(request, 'base.html' )
# HOME VIEW
def home(request):
    product_objects=Products.objects.all()
    # searching code
    item_name=request.GET.get('item_name')
    if item_name !=''and item_name is not None:
        product_objects=Products.objects.filter(title__icontains=item_name)
        
    # pagination code
    paginator=Paginator(product_objects,10)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)
    return render(request, 'home.html',  {'product_objects':product_objects} )

# CHECKOUT VIEW
def checkout(request):
    return render(request, 'checkout.html' )

# PRODUCT VIEW
def product(request):
    product_object=Products.objects.get(id=id,)
    return render(request, 'product.html')

# cart views
def cart(request):
    return render(request, 'cart.html')
