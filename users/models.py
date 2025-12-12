from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext, gettext_lazy as _

class Report(models.Model):
    text = models.CharField(max_length=6)

    def __str__(self):
        return self.text
    
class Notification(models.Model):
    """A notif in a report"""
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    message = models.OneToOneField('Refriends.Message', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string represenation of the model"""
        if message:
            return self.message
        else:
            return self.text