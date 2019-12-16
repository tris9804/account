from django.shortcuts import render
from rest_framework import viewsets
from .models import AccountBook, Category, Consume, Proportion
from .serializers import AccountBookSerializer, CategorySerializer, ConsumeSerializer, ProportionSerializer

class AccountBookViewSet(viewsets.ModelViewSet):
    queryset = AccountBook.objects.all()
    serializer_class = AccountBookSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ConsumeViewSet(viewsets.ModelViewSet):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer


class ProportionViewSet(viewsets.ModelViewSet):
    queryset = Proportion.objects.all()
    serializer_class = ProportionSerializer