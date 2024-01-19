import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Welcome(models.Model):
    id = models.BigAutoField(primary_key=True)
    welcome_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.welcome_text


class FileUploadNumberRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    login_user_id = models.BigIntegerField('login user id')
    file_type = models.IntegerField()
    file_upload_time = models.DateTimeField("file upload date time")

    def __str__(self):
        return f'FileType:{self.file_type},FileUploadTime:{self.file_upload_time}'

    def was_uploaded_recently(self):
        return self.file_upload_time >= timezone.now() - datetime.timedelta(days=7)


class FileSpeedLimitedConfiguration(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.IntegerField(
        db_comment="user type 1: anonymous user,2:login user")
    limited_qps = models.IntegerField(
        db_comment="limited qps. 1qps for anonymous user,10 qps  for  login user ")

    def __str__(self):
        return f'UserType:{self.user_type},LimitedQPS:{self.limited_qps}'


class SiteUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_serial_no = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64)
    last_login_date_time = models.DateTimeField()
    allowed_qps = models.IntegerField(default=10)
    user_login_status = models.IntegerField(
        db_comment="1: login 2: don't login", default=2)

    def __str__(self):
        return self.user_name
