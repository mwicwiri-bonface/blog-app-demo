from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from blog.forms import CategoryModelForm
from blog.models import Category, Blog


class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_blogs'] = Blog.objects.all()[:5]
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = "index.html"
    success_url = reverse_lazy("index")
