from django.shortcuts import render
from .models import AboutProduct, Product, Certification


def home_view(request):
    about = AboutProduct.objects.all()
    products = Product.objects.all()
    certifications = Certification.objects.all()
    context = {
        'abouts': about,
        'products': products,
        'certifications': certifications,
    }
    return render(request, 'home.html', context)

