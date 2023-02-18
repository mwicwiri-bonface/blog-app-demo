from django.urls import path

from accounts.decorators import decorate_url_patterns
from blog.views import CategoryCreateView, HomePage

app_name = "blog"

urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('create-category/', CategoryCreateView.as_view(), name="create-category")
]

decorate_url_patterns(patterns=urlpatterns, user_type="AU")
