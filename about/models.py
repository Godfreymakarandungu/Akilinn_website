from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField
    
class  About(models.Model):
    Title_Small  = models.CharField( max_length = 50 ,blank = False)
    Title_Big    = models.CharField( max_length = 50 ,blank = False)
    Content      = RichTextField()
    Button_Icon  = models.ImageField( upload_to="icons")
    Youtube_Link = models.CharField( max_length = 150)
    Picture      = models.ImageField( upload_to = "about")
    Button       = models.CharField( max_length = 30)
    # Video        = models.
    
    class Meta:
        db_table = "About"     
    
class Shoutout_One(models.Model):
    Title     = models.CharField( max_length = 50 ,blank = False)
    Content   = RichTextField()
    Picture   = models.ImageField( upload_to = "about", blank = False)
    Name      = models.CharField( max_length = 50 ,blank = False)
    Job_Title = models.CharField( max_length = 50 ,blank = False)
    
    class Meta:
            db_table = "Shoutout_One" 
class Shoutout_Two(models.Model):
    Title     = models.CharField( max_length = 50 ,blank = False)
    Content   = RichTextField()
    Picture   = models.ImageField( upload_to = "about", blank = False)
    Name      = models.CharField( max_length = 50 ,blank = False)
    Job_Title = models.CharField( max_length = 50 ,blank = False)
    
    class Meta:
            db_table = "Shoutout_Two" 
    
class Shoutout_Three(models.Model):
    Title     = models.CharField( max_length = 50 ,blank = False)
    Content   = RichTextField()
    Picture   = models.ImageField( upload_to = "about", blank = False)
    Name      = models.CharField( max_length = 50 ,blank = False)
    Job_Title = models.CharField( max_length = 50 ,blank = False)
    
    class Meta:
        db_table = "Shoutout_Three" 
        
class Shoutout_Four(models.Model):
    Title     = models.CharField( max_length = 50 ,blank = False)
    Content   = RichTextField()
    Picture   = models.ImageField( upload_to = "about", blank = False)
    Name      = models.CharField( max_length = 50 ,blank = False)
    Job_Title = models.CharField( max_length = 50 ,blank = False)
    
    class Meta:
        db_table = "Shoutout_Four"
        
class Features_About(models.Model):
    Title_Small = models.CharField( max_length = 50 ,blank = False)
    Title_Big   = models.CharField( max_length = 50 ,blank = False)
    Content     = RichTextField()
    Skills      = RichTextField()
    
    class Meta:
            db_table = "Features_About"    
  