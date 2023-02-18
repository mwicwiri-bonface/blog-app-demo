from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.forms import CategoryModelForm
from blog.models import Category


def home(request):
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "index.html", dict(form=form))


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = "index.html"
    success_url = reverse_lazy("index")
