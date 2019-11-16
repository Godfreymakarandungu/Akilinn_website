from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField


class Get_In_Touch(models.Model):
    Title        = models.TextField( max_length=50 , blank = False)
    Content      = RichTextField()
    Picture      = models.ImageField( upload_to = "contact")
    
    class Meta:
        db_table = "Get_In_Touch" 