from .models import ProductType, Product, Review
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def gettypes(request):
    types_list=ProductType.objects.all()
    context={'types_list' : types_list}
    return render(request, 'clubapp/types.html' , context=context) #{'type_list' : type_list})

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'clubapp/products.html', {'products_list': products_list})