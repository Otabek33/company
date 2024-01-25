from django.urls import path

from base.views import main_page

app_name = "main"

urlpatterns = [
    path("", main_page, name="main_page"),
]
