from django.shortcuts import render


# Create your views here.
def electronics(request):
    product_dict = {
        'product1': 'MAC',
        'product2': 'Apple',
        'product3': 'Samsung'
    }
    return render(request, 'products.html', product_dict)


def toys(request):
    product_dict = {
        'product1': 'Remote Car',
        'product2': 'Rocket',
        'product3': 'Truck'
    }
    return render(request, 'products.html', product_dict)


def shoes(request):
    product_dict = {
        'product1': 'Addidas',
        'product2': 'Nike',
        'product3': 'Reboke'
    }
    return render(request, 'products.html', product_dict)


def index(request):
    return render(request, 'index.html')
