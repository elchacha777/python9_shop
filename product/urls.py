from django.urls import path
from .views import homepage, products_list, product_details

urlpatterns = [
    path('', homepage, name='index-page'),
    path('products/<slug:category_slug>/',products_list, name='product-list'),
    path('products/details/<int:product_id>/', product_details, name="product-details"),
]
