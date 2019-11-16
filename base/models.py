from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField


class Navigation_Bar_Links(models.Model):
    #  def links():
        Home      = models.CharField(max_length = 50, blank = False, default = "home")
        About     = models.CharField(max_length = 50, blank = False, default = "home")
        Services  = models.CharField(max_length = 50, blank = False, default = "home")
        Blog      = models.CharField(max_length = 50, blank = False, default = "home")
        Contact   = models.CharField(max_length = 50, blank = False, default = "home")
        Careers   = models.CharField(max_length = 50, blank = False, default = "home")

       
        class Meta:
            db_table = "Navigation_Bar_Links" 
        
class Footer(models.Model):
        Content       = RichTextField()
        Picture_One   = models.ImageField( upload_to="footer")
        Picture_Two   = models.ImageField( upload_to="footer")
        Picture_Three = models.ImageField( upload_to="footer")
        Picture_Four  = models.ImageField( upload_to="footer")
        Picture_Five  = models.ImageField( upload_to="footer")
        Picture_Six   = models.ImageField( upload_to="footer")
        Picture_Seven = models.ImageField( upload_to="footer")
        Picture_Eight = models.ImageField( upload_to="footer")
       
        class Meta:
            db_table = "Footer" 
        
class Social_Media_Footer(models.Model):
        Facebook  = models.CharField( max_length = 50)
        Twitter   = models.CharField( max_length = 50)
        Instagram = models.CharField( max_length = 50)
        Whatsup   = models.CharField( max_length = 50)
        Telegram  = models.CharField( max_length = 50)
        LinkedIn  = models.CharField( max_length = 50)
        Youtube   = models.CharField( max_length = 50)
       
        class Meta:
            db_table = "Social_Media_Footer" 
        
class Others(models.Model):
        Phone_Number = PhoneNumberField()
        Email        = models.EmailField( max_length=254 ,blank = False) 
        Logo         = models.ImageField( upload_to="base" ,blank=False) 
        Icon_Title   = models.ImageField( upload_to="base" ,blank=False) 
        Logo_Icon    = models.ImageField( upload_to="base" ,blank=False) 
        
        class Meta:
            db_table = "Others" 
            