
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Product, News
from .serializers import ProductSerializer


def home(request):
    products = Product.objects.filter(is_available=True)
    news = News.objects.filter(published=True).order_by("-created_at")

    return render(
        request,
        "store/home.html",
        {"products": products, "news": news}
    )


class ProductListAPI(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.filter(
            is_available=True
        ).select_related("category", "brand").order_by("-created_at")
