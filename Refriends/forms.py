from django import forms

from .models import Group, Message
from django.utils.translation import gettext, gettext_lazy as _

class GroupForm(forms.ModelForm):
    text = forms.CharField(
        label=_("Name"),
        strip=False,
    )
    members = forms.CharField(
        label=_("Members"),
        strip=False,
        help_text= 'Write the usernames of those who will have access to this group, with correct case and separated by commas.'
    )
    all_users = forms.CheckboxInput()
    class Meta:
        model = Group
        fields = ['text', 'members', 'all_users']
        labels = {'text': ' ', 'members': ' ',}
        
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}