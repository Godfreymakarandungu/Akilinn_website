from django.shortcuts import render

# common imports
from base.models import Navigation_Bar_Links
from base.models import Footer
from base.models import Social_Media_Footer
from base.models import Others

from .models import Data_Agreement

def data_storage(request):
    # comon querryset
    Queryset_Navigation_links = Navigation_Bar_Links.objects.all()
    Queryset_Footer           = Footer.objects.all()
    Queryset_Social           = Social_Media_Footer.objects.all()
    Queryset_Others           = Others.objects.all()
    # end of common querryset
    Queryset_Data             = Data_Agreement.objects.all()

    return render(request,'useragreement.html',{ #common views
                                        "links"       : Queryset_Navigation_links,
                                        "footer"      : Queryset_Footer,
                                        "social"      : Queryset_Social,
                                        "others"      : Queryset_Others,
                                         #end ofcommon views
                                        "data"        : Queryset_Data,
                
                                        })                                      