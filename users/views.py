from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import UserCreationForm

# User pages views.


def register(request):
    """Register a new user"""
    if request.method != "POST":
        # No data submitted, create a blank form.
        form = UserCreationForm()
    else:
        # POST data submitted, process data.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("Refriends:info")
    # Display a blank/invalid form

    context = {"form": form}
    return render(request, "registration/register.html", context)
