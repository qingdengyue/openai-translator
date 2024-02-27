from django.urls import path

from . import views

app_name="translator"
urlpatterns = [
    path("", views.index, name="index"),
    path("files",views.HomePageView.as_view(),name="home"),
    path("files/upload",views.FormWithFilesView.as_view(),name="translator_file"),
]
