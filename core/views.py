from django.shortcuts import render, redirect
from core.models import Product, Category, Advertisement
from django.db.models import Q
from core.forms import ProductForm

def main(request):
    category_search = request.GET.get('search') if request.GET.get('search') != None else ''
    
    if category_search != '':
        products = Product.objects.filter(Q(category__name__icontains=category_search))
    else:
        products = Product.objects.all()
    
    categories = Category.objects.all()
    ads = Advertisement.objects.all()
    products_count = products.count()
    context = {'categories': categories, 'products': products, 'products_count': products_count, 'ads': ads}
    return render(request, 'core/main.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    name = product.name() # type: ignore
    category = product.category() # type: ignore   
    description = product.description() # type: ignore
    price = product.price() # type: ignore   
    date = product.created() # type: ignore   
    context = {'name': name, 'category': category, 'description': description, 'price': price, 'date': date}     
    return render(request, 'core/product.html', context)

def create_product(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect("main")
        
    context = {'form': form}
    return render(request, "core/product_form.html", context)

def edit_product(request, pk):
    form = ProductForm()
    
    # if request.method == 'GET':
        