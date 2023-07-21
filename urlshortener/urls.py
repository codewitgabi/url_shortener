from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("dashboard/", admin.site.urls),
    path("", include("home.urls")),
]


handler404 = "home.views.page_not_found"
