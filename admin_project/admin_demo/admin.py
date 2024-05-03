# admin_demo/admin.py
from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'published_date')
    search_fields = ['title', 'author__name']

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
