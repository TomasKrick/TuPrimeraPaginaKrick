from django.shortcuts import render
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm

def inicio(request):
    return render(request, "blog/inicio.html")


def crear_autor(request):
    mensaje = ""

    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Autor guardado con éxito."
            form = AutorForm()
    else:
        form = AutorForm()

    return render(
        request,
        "blog/formulario.html",
        {"form": form, "titulo": "Crear autor", "mensaje": mensaje},
    )


def crear_categoria(request):
    mensaje = ""

    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Categoría guardada con éxito."
            form = CategoriaForm()
    else:
        form = CategoriaForm()

    return render(
        request,
        "blog/formulario.html",
        {"form": form, "titulo": "Crear categoría", "mensaje": mensaje},
    )


def crear_post(request):
    mensaje = ""

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Post guardado con éxito."
            form = PostForm()
    else:
        form = PostForm()

    return render(
        request,
        "blog/formulario.html",
        {"form": form, "titulo": "Crear post", "mensaje": mensaje},
    )


def buscar_post(request):
    resultados = []
    form = BusquedaPostForm(request.GET or None)

    if form.is_valid():
        titulo_buscado = form.cleaned_data.get("titulo")
        if titulo_buscado:
            resultados = Post.objects.filter(titulo__icontains=titulo_buscado)

    return render(
        request,
        "blog/buscar.html",
        {"form": form, "resultados": resultados},
    )