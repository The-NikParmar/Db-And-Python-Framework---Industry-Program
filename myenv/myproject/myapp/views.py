from django.shortcuts import render,redirect,get_object_or_404
from django.http import request
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def add_product(request):
    if request.POST:
        id= Product_Mst.objects.create(product_name=request.POST['product_name'])
        if id:
            id= Product_Subcat.objects.create(

                product_id= id,
                product_price=request.POST["product_price"],
                product_image=request.FILES["product_image"],
                product_model=request.POST["product_model"],
                product_ram=request.POST["product_ram"],
            )
            messages.success(request,"Product Added Successfully...")
            return redirect('view_product')
        else:
            return render(request,"addproduct.html")
    return render(request,"add_product.html")


def view_product(request):
    product= Product_Mst.objects.all()
    products= Product_Subcat.objects.all()
    return render(request,"view_product.html",{'product':product,'products':products})
    

def edit_product(request, pk):
    product = get_object_or_404(Product_Subcat, pk=pk)
    if request.method == 'POST':
        product.product_price = request.POST['product_price']
        product.product_model = request.POST['product_model']
        product.product_ram = request.POST['product_ram']
        if 'product_image' in request.FILES:
            product.product_image = request.FILES['product_image']
        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect('view_product')
    return render(request, 'edit_product.html', {'product': product})

def search_product(request):
    query = request.GET.get('q')
    if query:
        products = Product_Mst.objects.filter(product_name__icontains=query)
    else:
        products = Product_Mst.objects.none()
    return render(request, 'search_product.html', {'products': products, 'query': query})

def delete_product(request, pk):
    product = get_object_or_404(Product_Mst, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully.")
    return redirect('index') 