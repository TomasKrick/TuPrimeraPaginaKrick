from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class Page(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    content = CKEditor5Field("Contenido")
    image = models.ImageField(upload_to="pages/", blank=True, null=True)
    published_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pages")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:page_detail", kwargs={"pk": self.pk})