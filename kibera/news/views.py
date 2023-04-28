from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
import django_filters.rest_framework
from django_filters import rest_framework as filters

class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_date')
    serializer_class = NewsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title',)




# Create your views here.
class NewsCreateAPIView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsUpdateAPIView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDestroyAPIView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
