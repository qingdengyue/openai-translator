from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import FileSpeedLimitedConfiguration, Question, Choice, FileUpload
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import FilesForm
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .ai_translator.model import OpenAIModel
from .ai_translator.translator import PDFTranslator
from .forms import getFormat, getLanguage

import uuid
import random
import os
upload_dir = os.path.join(settings.MEDIA_ROOT, 'file')
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)


class LocalFileSystemStorage(FileSystemStorage):
    pass


fs = LocalFileSystemStorage(location=upload_dir)


# Create your views here.

class GetParametersMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", None)
        context["size"] = self.request.GET.get("size", None)
        return context


class FormWithFilesView(GetParametersMixin, FormView):
    template_name = "translator/filetranslator.html"
    form_class = FilesForm
    success_url = "/files/download"

    def get_initial(self):
        return {}


def uploadFileAndTranslate(request):
    if request.method == 'POST':
        # 待翻译的 PDF文件
        pdfFile = request.FILES['file']

        # 转换后的语言和格式
        fileLanguage = getLanguage(request.POST.get("fileLanguage"))
        fileFormat = getFormat(request.POST.get("fileFormat"))

        print(f'TargetLanguage:{fileLanguage},TargetFormat:{fileFormat}')

        # 生成本地缓存的文件名称，并且保存文件信息，方便后续读取翻译
        _, file_extension = os.path.splitext(pdfFile.name)
        fileSavePath = f'{uuid.uuid4().hex}{file_extension}'
        saved_file_path = os.path.join(upload_dir, fileSavePath)
        with open(saved_file_path, "wb+") as destination:
            for chunk in pdfFile.chunks():
                destination.write(chunk)


        #解析文件后缀
        fileSuffix=".pdf"
        if fileFormat.lower() =='pdf':
            fileSuffix='.pdf'
        elif fileFormat.lower()=='markdown':
            fileSuffix='.md'    

        # 输出保存后的文件路径
        print(
            f'pdf file cached to: {saved_file_path}.will be removed after be translated')
        print(f'Start to translator')
        output_file_path = saved_file_path.replace(".pdf", f'_translated{fileSuffix}')

        # 加在OpenAI模型
        model = OpenAIModel(model="gpt-3.5-turbo",
                            api_key=os.environ["OPENAI_API_KEY"])

        # 初始化翻译
        translator = PDFTranslator(model)

        # 调用翻译方法进行文件处理
        translator.translate_pdf(
            saved_file_path, output_file_path=output_file_path, file_format=fileFormat, target_language=fileLanguage)
        # read pdf file and translate to en_US
        # save local file and gen url to front
        # 构造前端使用的URL地址方便用户下载
        return JsonResponse({
            "success": True,
            "downloadUrl": f"{settings.MEDIA_URL}file/{fileSavePath.replace(file_extension,f'_translated{fileSuffix}')}",
            "fileName": fileSavePath.replace(file_extension, f'_translated{fileSuffix}')
        })
    return JsonResponse({"success": True})
