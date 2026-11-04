
from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    ProductVariation,
    ProductImage,
    News,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "slug")
    list_filter = ("parent",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "category",
        "price",
        "is_available",
    )
    list_filter = ("brand", "category", "is_available")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        ProductImageInline,
        ProductVariationInline,
    ]


@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "name",
        "value",
        "price",
        "is_available",
    )
    list_filter = ("name", "is_available")
    search_fields = ("product__name", "value")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at")
    list_filter = ("published", "created_at")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
