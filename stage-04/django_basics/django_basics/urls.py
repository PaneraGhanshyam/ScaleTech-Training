from django.contrib import admin
from django.urls import path,include
# from users.views import UserListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    # path("", UserListView.as_view()),
    path("feedback/", include("feedback.urls")),

]