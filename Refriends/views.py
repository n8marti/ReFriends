import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import GroupForm, MessageForm
from .models import Group

common_timezones = {
    "UTC-12:00": "Etc/UTC-12",
    "UTC-11:00": "Etc/UTC-11",
    "UTC-10:00": "Pacific/Honolulu",
    "UTC-9:00": "America/Anchorage",
    "UTC-8:00": "America/Los_Angeles",
    "UTC-7:00": "America/Denver",
    "UTC-6:00": "America/Chicago",
    "UTC-5:00": "America/New_York",
    "UTC-4:00": "America/Halifax",
    "UTC-3:00": "America/Argentina/Buenos_Aires",
    "UTC-2:00": "Etc/GMT-2",
    "UTC-1:00": "Atlantic/Azores",
    "UTC": "Etc/UTC",
    "UTC+1:00": "Europe/Berlin",
    "UTC+2:00": "Europe/Helsinki",
    "UTC+3:00": "Europe/Moscow",
    "UTC+4:00": "Europe/Astrakhan",
    "UTC+5:00": "Asia/Yekaterinaburg",
    "UTC+6:00": "Asia/Dhaka",
    "UTC+7:00": "Asia/Bangkok",
    "UTC+8:00": "Asia/Shanghai",
    "UTC+9:00": "Asia/Tokyo",
    "UTC+10:00": "Australia/Sydney",
    "UTC+11:00": "Pacific/Guadalcanal",
    "UTC+12:00": "Pacific/Auckland",
}


@login_required
def set_timezone(request):
    if request.method == "POST":
        request.session["django_timezone"] = request.POST["timezone"]
        return redirect("Refriends:groups")
    else:
        return render(
            request, "Refriends/set_timezone.html", {"timezones": pytz.common_timezones}
        )


def index(request):
    if not request.user.is_authenticated:
        """The home page for ReFriends"""
        return render(request, "Refriends/index.html")
    else:
        return redirect("Refriends:groups")


@login_required
def groups(request):
    """Show all groups"""
    groups = Group.objects.order_by("date_added")
    context = {"groups": groups}
    return render(request, "Refriends/groups.html", context)


@login_required
def group(request, group_id):
    """Show a single group and all its messages."""
    group = get_object_or_404(Group, id=group_id)
    messages = group.message_set.order_by("-date_added")
    members = group.members
    all_users = group.all_users
    user_tz = request.session.get("timezone", "UTC")

    context = {
        "group": group,
        "messages": messages,
        "members": members,
        "all_users": all_users,
        "user_tz": user_tz,
    }

    if request.user.username in members or all_users:
        return render(request, "Refriends/group.html", context)
    else:
        return redirect("Refriends:groups")


@login_required
def new_group(request):
    """Add a new group"""
    if request.method != "POST":
        # No data submitted, create a blank form.
        form = GroupForm()
    else:
        # POST data submitted, process data.
        form = GroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Refriends:groups")
    # Display a blank/invalid form

    context = {"form": form}
    return render(request, "Refriends/new_group.html", context)


@login_required
def new_message(request, group_id):
    """Add a new message in a particular group"""
    group = Group.objects.get(id=group_id)

    if request.method != "POST":
        # No data submitted, create a blank form.
        form = MessageForm()
    else:
        # POST data submitted, process data.
        form = MessageForm(data=request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.group = group
            new_message.author = request.user
            new_message.save()
            return redirect("Refriends:group", group_id=group_id)
    # Display a blank/invalid form

    context = {"group": group, "form": form}
    return render(request, "Refriends/new_message.html", context)


@login_required
def info(request):
    return render(request, "Refriends/info.html")
