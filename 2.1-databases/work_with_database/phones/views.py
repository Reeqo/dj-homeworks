from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    template = 'catalog.html'
    if sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_objects = reversed(Phone.objects.all().order_by('price'))
    else:
        phone_objects = Phone.objects.all().order_by(sort)
    print(phone_objects)
    return render(request, template, {'phones': phone_objects})


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    return render(request, template, {'phone': phone_object.first()})
