
from django.urls import path
from .views import AuthorList, AuthorDetail, PublisherList, PublisherDetail, BookList, BookDetail, StoreList, StoreDetail

urlpatterns = [
    path('authors/', AuthorList.as_view()),
    path('author/<int:pk>', AuthorDetail.as_view()),
    path('publishers/', PublisherList.as_view()),
    path('publisher/<int:pk>', PublisherDetail.as_view()),
    path('books/', BookList.as_view()),
    path('book/<int:pk>', BookDetail.as_view()),
    path('stores/', StoreList.as_view()),
    path('store/<int:pk>', StoreDetail.as_view())
]