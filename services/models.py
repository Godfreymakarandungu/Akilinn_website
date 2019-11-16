from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField


class Service_One(models.Model):
    Favicon  = models.ImageField( upload_to="services" ,blank = False)
    Title    = models.CharField( max_length=30 ,blank = False)
    Content  = RichTextField()
  
    class Meta:
            db_table = "Service_One" 
            
class Service_Two(models.Model):
    Favicon  = models.ImageField( upload_to="services" ,blank = False)
    Title    = models.CharField( max_length=30 ,blank = False)
    Content  = RichTextField() 
  
    class Meta:
            db_table = "Service_Two" 
            
class Service_Three(models.Model):
    Favicon  = models.ImageField( upload_to="services" ,blank = False)
    Title    = models.CharField( max_length=30 ,blank = False)
    Content  = RichTextField()
  
    class Meta:
            db_table = "Service_Three" 
           
class Service_Four(models.Model):
    Favicon  = models.ImageField( upload_to="services" ,blank = False)
    Title    = models.CharField( max_length=30 ,blank = False)
    Content  = RichTextField()
  
    class Meta:
            db_table = "Service_Four" 
               
class Service_Five(models.Model):
    Favicon  = models.ImageField( upload_to="services" ,blank = False)
    Title    = models.CharField( max_length=30 ,blank = False)
    Content  = RichTextField()
  
    class Meta:
            db_table = "Service_Five" 

class Service_Six(models.Model):
    Favicon  = models.ImageField( upload_to="services" ,blank = False)
    Title    = models.CharField( max_length=30 ,blank = False)
    Content  = RichTextField()      
  
    class Meta:
            db_table = "Service_Six" 
    
class Features_Services(models.Model):
    Title_Small = models.CharField( max_length=20 , blank = False)
    Title_Big   = models.CharField( max_length=30 , blank = False)   
    Content     = RichTextField()
  
    class Meta:
            db_table = "Features_Services" 
    
class  Splash_One(models.Model):
    Title    = models.CharField( max_length = 50, blank = False)    
    Content  = RichTextField()
  
    class Meta:
            db_table = "Splash_One" 
    
class  Splash_Two(models.Model):
    Title    = models.CharField( max_length = 50, blank = False)    
    Content  = RichTextField()
  
    class Meta:
            db_table = "Splash_Two"   
    
class  Splash_Three(models.Model):
    Title    = models.CharField( max_length = 50, blank = False)    
    Content  = RichTextField()
  
    class Meta:
            db_table = "Splash_Three"      