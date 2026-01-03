from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    """A group to chat in"""

    text = models.CharField(
        max_length=50,
        blank=True,
    )
    date_added = models.DateTimeField(auto_now_add=True)
    members = models.CharField(max_length=200)
    all_users = models.BooleanField()

    def __str__(self):
        """Return a string represenation of the model"""
        return self.text


class Message(models.Model):
    """A message in a group"""

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string represenation of the model"""
        return self.text
