from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ShopView, ProductDetailView, development, panels_page, DoorsHome

urlpatterns = [
    path('', DoorsHome.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('panels_page/', panels_page, name='panels_page'),
    path('development/', development, name='development'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

