from django.shortcuts import render

 # common imports
from base.models import Navigation_Bar_Links
from base.models import Footer
from base.models import Social_Media_Footer
from base.models import Others
# end of common imports
from home.models import Map_area

from .models import Get_In_Touch

def contact(request):
     # comon querryset
    Queryset_Navigation_links = Navigation_Bar_Links.objects.all()
    Queryset_Footer           = Footer.objects.all()
    Queryset_Social           = Social_Media_Footer.objects.all()
    Queryset_Others           = Others.objects.all()
    # end of common querryset
    #     map area
    Queryset_Map= Map_area.objects.all()
    
    Queryset_Contact          = Get_In_Touch.objects.all()
    
    return render(request,'contact.html',{#common views
                                        "links"         : Queryset_Navigation_links,
                                        "footer"        : Queryset_Footer,
                                        "social"        : Queryset_Social,
                                        "others"        : Queryset_Others,
                                         #end ofcommon views
                                        "map"           : Queryset_Map,
                                        "contact"       : Queryset_Contact,                                        
                                         })
    