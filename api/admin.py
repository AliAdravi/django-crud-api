from django.contrib import admin

from .models import Author, Publisher, Book, Store

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display= ['name', 'age']
admin.site.register(Author, AuthorAdmin)

admin.site.register(Publisher)

class BookAdmin(admin.ModelAdmin):
    fields = ['name', 'pages', 'price', 'rating', 'pubdate', 'authors']
    list_display = ['name', 'pages', 'price', 'rating', 'pubdate', 'get_authors']
    
    def get_authors(self, obj):
        return ", ".join([p.name for p in obj.authors.all()])
    
admin.site.register(Book, BookAdmin)

admin.site.register(Store)

