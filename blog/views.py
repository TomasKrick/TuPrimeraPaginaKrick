from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Page
from .forms import PageForm


def home(request):
    return render(request, "blog/home.html")


def about(request):
    return render(request, "blog/about.html")


class PageListView(ListView):
    model = Page
    template_name = "blog/page_list.html"
    context_object_name = "pages"
    ordering = ["-published_date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(subtitle__icontains=q)
            )
        return queryset


class PageDetailView(DetailView):
    model = Page
    template_name = "blog/page_detail.html"
    context_object_name = "page"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "blog/page_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "blog/page_form.html"

    def get_queryset(self):
        return Page.objects.filter(author=self.request.user)


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "blog/page_confirm_delete.html"
    success_url = reverse_lazy("blog:page_list")

    def get_queryset(self):
        return Page.objects.filter(author=self.request.user)