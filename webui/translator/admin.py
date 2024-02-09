from django.contrib import admin

# Register your models here.
from .models import Welcome, FileSpeedLimitedConfiguration, FileUploadNumberRecord, SiteUser,Question,Choice,FileUpload

admin.site.register(Welcome)
admin.site.register(FileSpeedLimitedConfiguration)
admin.site.register(FileUploadNumberRecord)
admin.site.register(SiteUser)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(FileUpload)
