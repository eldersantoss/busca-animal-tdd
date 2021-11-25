from django.urls import path

from animais.views import index


urlpatterns = [
    path("", index, name="index"),
]
