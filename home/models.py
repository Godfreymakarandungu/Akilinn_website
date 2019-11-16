from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField




class Carousel_One(models.Model):
    #  def colousel():
        Title_line_one   = models.CharField(max_length = 80, blank = False)
        Title_line_two   = models.CharField(max_length = 80, blank = False)        
        Content          = models.CharField(max_length = 30, blank = False)
        Button           = models.CharField(max_length = 10, blank = False)
        Image            = models.ImageField(  upload_to = "home")
       
        class Meta:
            db_table = "Carousel_One"  

class Carousel_Two(models.Model):
    #  def colousel():
        Title_line_one  = models.CharField(max_length = 80, blank = False)
        Title_line_two  = models.CharField(max_length = 80, blank = False)
        Content         = models.CharField(max_length = 30, blank = False)                
        Button          = models.CharField(max_length = 10, blank = False)
        Image           = models.ImageField(  upload_to = "home")
       
        class Meta:
            db_table = "Carousel_Two"  

class Carousel_Three(models.Model):
    #  def colousel():
        Title_line_one   = models.CharField(max_length = 80, blank = False)
        Title_line_two   = models.CharField(max_length = 80, blank = False)
        Content          = models.CharField(max_length = 30, blank = False)        
        Button           = models.CharField(max_length = 10, blank = False)
        Image            = models.ImageField(  upload_to = "home")
       
        class Meta:
            db_table = "Carousel_Three"  
    
class Surprise_New(models.Model):
        Icon           = models.ImageField(  upload_to="icons")
        Small_Content  = models.CharField(max_length = 50 ,blank = False)      
        Big_Content    = models.CharField(max_length = 50 ,blank = False)      
       
        class Meta:
            db_table = "Surprise"  
 
class Brand_One(models.Model):
        Icon    = models.ImageField(   upload_to="icons")
        Title   = models.CharField( max_length  = 30 ,blank =False)
        Content = RichTextField()
        Button  = models.CharField( max_length = 20, blank = False ,default = "Read More")
        Link    = models.CharField( max_length=50 ,blank =False ,default = "home")
        
       
        class Meta:
            db_table = "Brand_One"  
 
class Brand_Two(models.Model):
        Icon    = models.ImageField(   upload_to="icons")
        Title   = models.CharField( max_length  = 30 ,blank =False)
        Content = RichTextField()
        Button  = models.CharField( max_length = 20, blank = False ,default = "Read More") 
        Link    = models.CharField( max_length=50 ,blank =False ,default = "home")
       
        class Meta:
            db_table = "Brand_Two"  
 
        
class Brand_Three(models.Model):
        Icon    = models.ImageField(   upload_to="icons")
        Title   = models.CharField( max_length  = 30 ,blank =False)
        Content = RichTextField()
        Button  = models.CharField( max_length = 20, blank = False ,default = "Read More")
        Link    = models.CharField( max_length=50 ,blank =False ,default = "home")
       
        class Meta:
            db_table = "Brand_Three"  
        
class Referee_One(models.Model):
        Title       = models.CharField( max_length = 50 ,blank  = False)
        Content     = RichTextField()
        Profile_Pic = models.ImageField(   upload_to = "home" ,blank = False)
        Name        = models.CharField( max_length=30 ,blank = False)
        Job_Title   = models.CharField( max_length=50 ,blank = False)
       
        class Meta:
            db_table = "Referee_One"
                    
class Referee_Two(models.Model):
        Title       = models.CharField( max_length = 50 ,blank  = False)
        Content     = RichTextField()
        Profile_Pic = models.ImageField(   upload_to = "home" ,blank = False)
        Name        = models.CharField( max_length=30 ,blank = False)
        Job_Title   = models.CharField( max_length=50 ,blank = False)
       
        class Meta:
            db_table = "Referee_Two"
                    
class Referee_Three(models.Model):
        Title       = models.CharField( max_length = 50 ,blank  = False)
        Content     = RichTextField()
        Profile_Pic = models.ImageField(   upload_to = "home" ,blank = False)
        Name        = models.CharField( max_length=30 ,blank = False)
        Job_Title   = models.CharField( max_length=50 ,blank = False)
       
        class Meta:
            db_table = "Referee_Three"
class Discover(models.Model):
        Title_Small = models.CharField( max_length = 50 ,blank  = False)
        Title       = models.CharField( max_length = 60 ,blank  = False)
        Content     = RichTextField()
        Picture     = models.ImageField(   upload_to = "home" ,blank = False)
       
        class Meta:
            db_table = "Discover"
        
class Team(models.Model):
        Title_Small   = models.CharField( max_length = 50 ,blank  = False)
        Title_Big     = models.CharField( max_length = 50 ,blank  = False)
        Content       = RichTextField()
        Picture_One   = models.ImageField(   upload_to = "home" ,blank = False)
        Picture_Two   = models.ImageField(   upload_to = "home" ,blank = False)
        Picture_Three = models.ImageField(   upload_to = "home" ,blank = False)
        Picture_Four  = models.ImageField(   upload_to = "home" ,blank = False)
        Bullet_One    = models.CharField( max_length = 25 ,blank  = False)    
        Bullet_Two    = models.CharField( max_length = 25 ,blank  = False)    
        Bullet_Three  = models.CharField( max_length = 25 ,blank  = False)    
        Bullet_Four   = models.CharField( max_length = 25 ,blank  = False)    
        Bullet_Five   = models.CharField( max_length = 25 ,blank  = False) 
       
        class Meta:
            db_table = "Team"   
        
class Contact(models.Model):
        Title        = models.CharField( max_length = 50 ,blank  = False)
        Content      = RichTextField()
       
        class Meta:
            db_table = "Contact"
class Map_area(models.Model):
        Background_Image = models.ImageField(   upload_to="home")
        Title            = models.CharField( max_length = 50 ,blank = False)
        Location         = models.CharField( max_length = 50 ,blank = False)
        Country          = models.CharField( max_length = 50 ,blank = False)
       
        class Meta:
            db_table = "Map_Area"