from django.shortcuts import render

# common imports
from base.models import Navigation_Bar_Links
from base.models import Others

# end of common imports

from .models import Error404
from .models import Error500

                                       
def fourOfour(request):
        # comon querryset
    Queryset_Others              = Others.objects.all()
    Queryset_Navigation_links    = Navigation_Bar_Links.objects.all()
    # end of common querryset
    Queryset_Error404            = Error404.objects.all()
    
    return render(request,'404.html',{ #common views
                                        "links"            : Queryset_Navigation_links,
                                        "others"           : Queryset_Others,
                                         #end ofcommon views
                                         "error404"        : Queryset_Error404,
                                        } ,status=404)


def fivehundred(request):
    # comon querryset
    Queryset_Others              = Others.objects.all()
    Queryset_Navigation_links    = Navigation_Bar_Links.objects.all()
    # end of common querryset
    Queryset_Error500            = Error500.objects.all()
    
    return render(request,'500.html',{ #common views
                                        "links"            : Queryset_Navigation_links,
                                        "others"           : Queryset_Others,                                         
                                         #end ofcommon views
                                         "error500"        : Queryset_Error500,
                                        } ,status = 500)