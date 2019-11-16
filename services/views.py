from django.shortcuts import render

 # common imports
from base.models import Navigation_Bar_Links
from base.models import Footer
from base.models import Social_Media_Footer
from base.models import Others
# end of common imports

from .models import Service_One
from .models import Service_Two
from .models import Service_Three
from .models import Service_Four
from .models import Service_Five
from .models import Service_Six
from .models import Features_Services
from .models import Splash_One
from .models import Splash_Two
from .models import Splash_Three
     
def services(request):
    # comon querryset
    Queryset_Navigation_links = Navigation_Bar_Links.objects.all()
    Queryset_Footer           = Footer.objects.all()
    Queryset_Social           = Social_Media_Footer.objects.all()
    Queryset_Others           = Others.objects.all()
    Queryset_Service_one      = Service_One.objects.all()
    Queryset_Service_two      = Service_Two.objects.all()
    Queryset_Service_three    = Service_Three.objects.all()
    Queryset_Service_four     = Service_Four.objects.all()
    Queryset_Service_five     = Service_Five.objects.all()
    Queryset_Service_six      = Service_Six.objects.all()
    Queryset_Features         = Features_Services.objects.all()
    Queryset_Splash_one       = Splash_One.objects.all()
    Queryset_Splash_two       = Splash_Two.objects.all()
    Queryset_Splash_three     = Splash_Three.objects.all()
    # end of common querryset
    return render(request,'service.html',{#common views
                                        "links"         : Queryset_Navigation_links,
                                        "footer"        : Queryset_Footer,
                                        "social"        : Queryset_Social,
                                        "others"        : Queryset_Others,
                                         #end ofcommon views
                                        "serviceone"    : Queryset_Service_one,
                                        "servicetwo"    : Queryset_Service_two,
                                        "servicethree"  : Queryset_Service_three,
                                        "servicefour"   : Queryset_Service_four,
                                        "servicefive"   : Queryset_Service_five,
                                        "servicesix"    : Queryset_Service_six,
                                        "features"      : Queryset_Features,
                                        "splashone"     : Queryset_Splash_one,
                                        "splashtwo"    : Queryset_Splash_two,
                                        "splashthree"   : Queryset_Splash_three,
                                         })
    