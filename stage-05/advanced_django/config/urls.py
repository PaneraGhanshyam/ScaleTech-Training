"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # ---------- DRF Token Auth ----------
    path("api/token/", obtain_auth_token, name="api_token"),

    # ---------- JWT Auth ----------
    path(
        "api/jwt/token/",
        TokenObtainPairView.as_view(),
        name="jwt_obtain_pair",
    ),
    path(
        "api/jwt/token/refresh/",
        TokenRefreshView.as_view(),
        name="jwt_token_refresh",
    ),
    path(
        "api/jwt/token/verify/",
        TokenVerifyView.as_view(),
        name="jwt_token_verify",
    ),

    # ---------- OAuth2 ----------
    path("o/", include(oauth2_urls)),

    # ---------- App URLs ----------
    path("api/", include("tasks.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
