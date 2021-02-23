from django.urls import path
from .views import homepage, ProductsDetailsView, HomePageView, ProductListView

urlpatterns = [
    path('', HomePageView.as_view(), name='index-page'),
    path('products/<slug:category_slug>/', ProductListView.as_view(), name='product-list'),
    path('products/details/<int:pk>/', ProductsDetailsView.as_view(), name="product-details"),
]
