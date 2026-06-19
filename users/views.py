import pytz
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import UserCreationForm


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        tz = self.request.POST.get("timezone")
        if tz in pytz.all_timezones:
            self.request.session["django_timezone"] = tz
        return response


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
