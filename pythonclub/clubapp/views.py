from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product, Review
from .forms import ProductForm, ReviewForm

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

# form view

def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'clubapp/newproduct.html', {'form': form})

def newReview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm
     return render(request, 'clubapp/newreview.html', {'form' : form})



