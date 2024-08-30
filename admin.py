<<<<<<< HEAD
from django.contrib import admin
from .models import Book

admin.site.register(Book)
=======
# admin.py

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
>>>>>>> origin/main
