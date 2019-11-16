"""Akilinn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from organizations.backends import invitation_backend
# from two_factor.urls import urlpatterns as tf_urls
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [  
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('blog/', include('zinnia.urls')),
    path('comments/', include('django_comments.urls')),
    path('testadmin', include('django_prometheus.urls')),
    path('sentry-debug/', trigger_error),#sentry
    path('ckeditor/', include('ckeditor_uploader.urls')),

    
    # site
    path('', include('home.urls')),
    path('home', include('home.urls')),
    path('about', include('about.urls')),
    path('contact', include('contact.urls')),
    path('services', include('services.urls')),
    path('careers', include('careers.urls')),
    path('datastorageagreement', include('agreements.urls')),
    path('email_subscription', include('user_data.urls')),
]
    
handler404='errors.views.fourOfour'
handler404='errors.views.fivehundred'
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
PROMETHEUS_EXPORT_MIGRATIONS = False
from django.urls import path



CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}