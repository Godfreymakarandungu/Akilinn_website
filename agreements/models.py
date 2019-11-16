from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField
 
class Data_Agreement(models.Model):
    Day      = models.IntegerField()
    Month    = models.IntegerField()
    Year     = models.CharField( max_length = 20)
    Title    = models.CharField( max_length = 50)
    Content  = RichTextField()
    Picture  = models.ImageField( upload_to = "agreement" ,blank=False)
    
    class Meta:
                db_table = "Data_Agreement" 