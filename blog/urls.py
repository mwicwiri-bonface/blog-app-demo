from django.urls import path

from blog.views import home, CategoryCreateView

urlpatterns = [
    path('', home, name="index"),
    path('create-category/', CategoryCreateView.as_view(), name="create-category")
]