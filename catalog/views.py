from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    print(f"--- Тип запроса: {request.method} ---")
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} получено.")
    return render(request, 'contacts.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


def main(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/main.html', context)
