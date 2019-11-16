from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField
 
            
class Head(models.Model):
    Picture  = models.ImageField( upload_to = "careers")
    Day      = models.IntegerField()
    Month    = models.IntegerField()
    Year     = models.CharField( max_length = 20)
    class Meta:
                db_table = "Head" 
    

class Career_One(models.Model):
        Title      = models.CharField(max_length = 50, blank = False, default = "home")
        Content    = RichTextField()
        class Meta:
                db_table = "Career_One" 
        
class Career_Two(models.Model):
        Title      = models.CharField(max_length = 50, blank = False, default = "home")
        Content    = RichTextField()
        class Meta:
                 db_table = "Career_Two" 
        
class Career_Three(models.Model):
        Title      = models.CharField(max_length = 50, blank = False, default = "home")
        Content    = RichTextField()
        class Meta:
                 db_table = "Career_Three" 
        
class Career_Four(models.Model):
        Title      = models.CharField(max_length = 50, blank = False, default = "home")
        Content    = RichTextField()
        class Meta:
                 db_table = "Career_Four" 
        
class Career_Five(models.Model):
        Title      = models.CharField(max_length = 50, blank = False, default = "home")
        Content    = RichTextField()
        class Meta:
                 db_table = "Career_Five" 
        
