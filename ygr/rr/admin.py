from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author",'get_categories')
    list_filter = ("author", "categories")
    search_fields = ("title",)
    filter_horizontal = ("categories",)

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])