from django import forms
from django.contrib.auth.models import User
from .models import PrivateMessage

class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ["receiver", "subject", "body"]

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["receiver"].queryset = User.objects.exclude(pk=user.pk)