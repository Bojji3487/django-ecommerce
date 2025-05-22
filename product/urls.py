from django.urls import path
from django.urls import path
from .views import CategoryListAPIView, ProductListAPIView, products

urlpatterns = [
    path('api/categories/', CategoryListAPIView.as_view(), name='api-categories'),
    path('api/products/', ProductListAPIView.as_view(), name='api-products'),
    path('', products, name='products'),
]