from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GroupForm, MessageForm
from .models import Group


def index(request):
    """The home page for ReFriends"""
    return render(request, "Refriends/index.html")


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

    context = {
        "group": group,
        "messages": messages,
        "members": members,
        "all_users": all_users,
    }
    members = str(members).split(", ")
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
    """Info page about the project."""
    return render(request, "Refriends/info.html")
