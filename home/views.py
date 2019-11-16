from django.shortcuts import render,redirect

# common imports
from base.models import Navigation_Bar_Links
from base.models import Footer
from base.models import Social_Media_Footer
from base.models import Others
# end of common imports

from .models import Carousel_One
from .models import Carousel_Two
from .models import Carousel_Three
from .models import Surprise_New
from .models import Brand_One
from .models import Brand_Two
from .models import Brand_Three
from .models import Referee_One
from .models import Referee_Two
from .models import Referee_Three
from .models import Discover
from .models import Team
from .models import Contact
from .models import Map_area

def home(request):
    # comon querryset
    Queryset_Navigation_links = Navigation_Bar_Links.objects.all()
    Queryset_Footer           = Footer.objects.all()
    Queryset_Social           = Social_Media_Footer.objects.all()
    Queryset_Others           = Others.objects.all()
    # end of common querryset
    Queryset_Carousel_One     = Carousel_One.objects.all()
    Queryset_Carousel_Two     = Carousel_Two.objects.all()
    Queryset_Carousel_Three   = Carousel_Three.objects.all()
    Queryset_Surprise         = Surprise_New.objects.all()
    Queryset_Brand_One        = Brand_One.objects.all()
    Queryset_Brand_Two        = Brand_Two.objects.all()
    Queryset_Brand_Three      = Brand_Three.objects.all()
    Queryset_Refereeone       = Referee_One.objects.all()
    Queryset_Refereetwo       = Referee_Two.objects.all()
    Queryset_Refereethree     = Referee_Three.objects.all()
    Queryset_Discover         = Discover.objects.all()
    Queryset_Team             = Team.objects.all()
    Queryset_Contact          = Contact.objects.all()
    Queryset_Map              = Map_area.objects.all()
    
    return render(request,'index.html',{ #common views
                                        "links"         : Queryset_Navigation_links,
                                        "footer"        : Queryset_Footer,
                                        "social"        : Queryset_Social,
                                        "others"        : Queryset_Others,
                                         #end ofcommon views
                                        "carouselone"   : Queryset_Carousel_One,
                                        "carouseltwo"   : Queryset_Carousel_Two,
                                        "carouselthree" : Queryset_Carousel_Three,
                                        "surprise"      : Queryset_Surprise,
                                        "brandone"      : Queryset_Brand_One,
                                        "brandtwo"      : Queryset_Brand_Two,
                                        "brandthree"    : Queryset_Brand_Three,
                                        "refereeone"    : Queryset_Refereeone,
                                        "refereetwo"    : Queryset_Refereetwo,
                                        "refereethree"  : Queryset_Refereethree,
                                        "discover"      : Queryset_Discover,
                                        "team"          : Queryset_Team,
                                        "contact"       : Queryset_Contact,
                                        "map"           : Queryset_Map,
                                        })
    
# redirecting user when path is empty
def home_redirect(request):
     return redirect("/home")
 