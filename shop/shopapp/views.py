from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product


# def index(request):
#     product = Product.objects.all()
#     context = {
#         'pr': product,
#     }
#     return render(request, 'index.html', context)
#
#
# def shop(request):
#     product = Product.objects.all()
#     context = {'pr': product}
#     return render(request, 'shop.html', context)
#
#
# def product_detail(request, slug):
#     product = Product.objects.get(slug=slug)
#     context = {'pr': product}
#     return render(request, 'product_detail.html', context)


def panels_page(request):
    return render(request, 'mdf_panels.html')


def not_found_404_error(request, exception):
    return render(request, '404.html')


def development(request):
    return render(request, 'development.html')


class DoorsHome(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'pr'


class ShopView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'pr'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'pr'
