from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "email"]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "categoria"]


class BusquedaPostForm(forms.Form):
    titulo = forms.CharField(
        max_length=100,
        required=False,
        label="Buscar por título"
    )