from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            viewer_group, _ = Group.objects.get_or_create(
                name="Viewer"
            )

            user.groups.add(viewer_group)

            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


@login_required
def dashboard_view(request):
    return render(
        request,
        "accounts/dashboard.html",
    )