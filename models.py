from django.db import models


class Email_Newsletter(models.Model):
    Email = models.EmailField(max_length=254)
    Time  = models.DateTimeField( auto_now_add=True, blank=False)