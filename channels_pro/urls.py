from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("login.urls")),
    path("", include("django.contrib.auth.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
