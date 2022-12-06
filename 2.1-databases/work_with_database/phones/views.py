from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    
    sort = request.GET.get('sort')

    if sort == 'name':
        phone_objects = Phone.objects.order_by('name')

    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')

    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')

    else:
        phone_objects = Phone.objects.all()


    phones = {'phones':[]}

    for phone in phone_objects:
        new_phone = {
            'id':phone.id,
            'name':phone.name,            
            'image':phone.image,
            'price':phone.price,
            'release_date':phone.release_date,
            'lte_exists':phone.lte_exists,
            'slug':phone.slug
            }
        phones['phones'].append(new_phone)
    
    context = phones
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=f'{slug}')

    for phone in phone_objects:
        context = {'phone':{
            'id':phone.id,
            'name':phone.name,            
            'image':phone.image,
            'price':phone.price,
            'release_date':phone.release_date,
            'lte_exists':phone.lte_exists,
            'slug':phone.slug}
            }

    return render(request, template, context)