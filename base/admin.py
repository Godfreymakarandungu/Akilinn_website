from django.contrib import admin


from base.models import Navigation_Bar_Links
from base.models import Footer
from base.models import Social_Media_Footer
from base.models import Others


admin.site.register(Navigation_Bar_Links)
admin.site.register(Footer)
admin.site.register(Social_Media_Footer)
admin.site.register(Others)