from django.shortcuts import render
from django.views.generic import ListView

from .models import UserProfile


# def home(request):
#     users = UserProfile.objects.all()

#     return render(
#         request,
#         "users/home.html",
#         {"users": users}
#     )

class UserListView(ListView):
    model = UserProfile
    template_name = "users/home.html"
    context_object_name = "users"