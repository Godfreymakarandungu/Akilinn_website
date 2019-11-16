from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField


class Error404(models.Model):
    Content = RichTextField()
    class Meta:
            db_table = "Error404" 
class Error500(models.Model):
    Content = RichTextField()
    class Meta:
        db_table = "Error500" 