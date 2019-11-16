from django.contrib import admin

from .models import About
from .models import Shoutout_One
from .models import Shoutout_Two
from .models import Shoutout_Three
from .models import Shoutout_Four
from .models import Features_About

admin.site.register(About)
admin.site.register(Shoutout_One)
admin.site.register(Shoutout_Two)
admin.site.register(Shoutout_Three)
admin.site.register(Shoutout_Four)
admin.site.register(Features_About)
