
from django.contrib import admin
from .models import Category, Product, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "slug")
    list_filter = ("parent",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available")
    list_filter = ("category", "is_available")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at")
    list_filter = ("published", "created_at")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
