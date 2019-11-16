from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Email_Newsletter(models.Model):
    Email= models.EmailField(max_length=254)
    Tieme= models.DateTimeField(auto_now_add=False)
    class meta:
        db_name="Email_Newsletter"