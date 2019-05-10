from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product, Review

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def gettypes(request):
    types_list=ProductType.objects.all()
    context={'types_list' : types_list}
    return render(request, 'clubapp/types.html' , context=context) 

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'clubapp/products.html', {'products_list': products_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    reviewcount=Review.objects.filter(product=id).count()
    reviews=Review.objects.filter(product=id)
    context={
        'prod' : prod,
        'reviewcount' : reviewcount,
        'reviews' : reviews,
    }
    return render(request, 'clubapp/proddetails.html', context=context)



