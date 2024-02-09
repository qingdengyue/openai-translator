from django.urls import path

from . import views

app_name="translator"
urlpatterns = [
    path("", views.index, name="index"),
    path("specifics/<int:config_id>/",views.detail,name="detail"),
    path("questionindex",views.QuestionIndexView.as_view(),name="questionindex"),
    path("questiondetail/<int:pk>",views.QuestionDetailView.as_view(),name="questiondetail"),
    path("questiondetail/<int:pk>/results",views.QuestionResultsView.as_view(),name="questionresults"),
    path("questiondetail/<int:question_id>/vote",views.questionvote,name="questionvote"),
    path("files",views.HomePageView.as_view(),name="home"),
    path("files/upload",views.CreateFileTranslatorView.as_view(),name="translator_file"),
]
