from django.urls import path

from . import views

app_name="translator"
urlpatterns = [
    path("", views.FormWithFilesView.as_view(), name="index"),
    path("files/upload",views.FormWithFilesView.as_view(),name="translator_file"),
    path("files/uploadFileAndTranslate",views.uploadFileAndTranslate,name="uploadFileAndTranslate"),
]
