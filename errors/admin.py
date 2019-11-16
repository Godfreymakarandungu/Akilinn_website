from django.contrib import admin

from .models import Error404
from .models import Error500

admin.site.register(Error404)
admin.site.register(Error500)