from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Page
        fields = ["title", "subtitle", "content", "image", "published_date"]