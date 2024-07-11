
from rest_framework import generics
#from django.urls import url
#from rest_framework_swagger.views import get_swagger_view

from .models import Author, Publisher, Book, Store
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer, StoreSerializer
# Create your views here.

class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class PublisherList(generics.ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    

class StoreList(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    

# Swagger
# schema_view = get_swagger_view(title='Pastebin API')

# urlpatterns = [
#     url(r'^$', schema_view)
# ]