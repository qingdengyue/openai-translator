from django.shortcuts import render
from django.http import HttpResponse
from .models import  FileSpeedLimitedConfiguration
from django.template import loader
# Create your views here.
def index(request):
    file_speed_limited_configuration_list=FileSpeedLimitedConfiguration.objects.order_by("id")[:2]
    template=loader.get_template("translator/index.html")
    context={
        "file_speed_limited_configuration_list":file_speed_limited_configuration_list
    }
    return HttpResponse(template.render(context,request))
