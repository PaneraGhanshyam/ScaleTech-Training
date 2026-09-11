from django.contrib import admin
from django.urls import path
from users.views import UserListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", UserListView.as_view()),
]