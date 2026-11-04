
from django.contrib import admin
from django.urls import path, include
from store.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("store.urls")),
    path("", home, name="home"),
]
