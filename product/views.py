from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer

def products(request):
    return render(request,'<h1>Products</h1>')