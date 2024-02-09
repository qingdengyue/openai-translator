from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import FileSpeedLimitedConfiguration, Question, Choice,FileUpload
from django.shortcuts import render, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views import generic
from .forms import FileTranslatorForm

# Create your views here.
def index(request):
    file_speed_limited_configuration_list = FileSpeedLimitedConfiguration.objects.order_by("id")[:2]
    context = {
        "file_speed_limited_configuration_list": file_speed_limited_configuration_list
    }
    return render(request, "translator/index.html", context)


def detail(request, config_id):
    try:
        configuration = get_object_or_404(FileSpeedLimitedConfiguration, pk=config_id)
    except FileSpeedLimitedConfiguration.DoesNotExist:
        raise Http404("Configuration does not exist")
    return render(request, "translator/detail.html", {"configuration": configuration})


def questionindex(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "translator/question/index.html", context)

class QuestionIndexView(generic.ListView):
   template_name="translator/question/index.html"
   context_object_name="latest_question_list"

   def get_queryset(self):
       return Question.objects.order_by("-pub_date")[:5]


class QuestionDetailView(generic.DetailView):
      model = Question
      template_name = "translator/question/detail.html"


class QuestionResultsView(generic.DetailView):
      model = Question
      template_name = "translator/question/results.html"

def questiondetail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "translator/question/detail.html", {"question": question})


def questionresults(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "translator/question/results.html", {"question": question})


def questionvote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("translator:questionresults", args=(question.id,)))


class HomePageView(generic.ListView):
    model = FileUpload
    template_name = "translator/home.html"


class CreateFileTranslatorView(generic.CreateView):
    model = FileUpload
    form_class = FileTranslatorForm
    template_name = "translator/filetranslator.html"
    success_url =reverse_lazy("translator:home")