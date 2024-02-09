from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import  FileSpeedLimitedConfiguration
from django.shortcuts import render,get_object_or_404
# Create your views here.
def index(request):
    file_speed_limited_configuration_list=FileSpeedLimitedConfiguration.objects.order_by("id")[:2]
    context={
        "file_speed_limited_configuration_list":file_speed_limited_configuration_list
    }
    return render(request,"translator/index.html",context)

def detail(request,config_id):
    try:
      configuration=FileSpeedLimitedConfiguration.objects.get(pk=config_id)
    except FileSpeedLimitedConfiguration.DoesNotExist:
        raise Http404("Configuration does not exist")
    return render(request,"translator/detail.html",{"configuration":configuration})
