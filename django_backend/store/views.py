from django.shortcuts import render
from .models import Product, News

def home(request):
    products = Product.objects.filter(is_available=True)
    news = News.objects.filter(published=True).order_by("-created_at")

    return render(request, "store/home.html", {
        "products": products,
        "news": news,
    })