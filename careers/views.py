from django.shortcuts import render

# common imports
from base.models import Navigation_Bar_Links
from base.models import Footer
from base.models import Social_Media_Footer
from base.models import Others
# end of common imports
from .models import Head
from .models import Career_One
from .models import Career_Two
from .models import Career_Three
from .models import Career_Four
from .models import Career_Five
def careers(request):
    # comon querryset
    Queryset_Navigation_links = Navigation_Bar_Links.objects.all()
    Queryset_Footer           = Footer.objects.all()
    Queryset_Social           = Social_Media_Footer.objects.all()
    Queryset_Others           = Others.objects.all()
    # end of common querryset
    Queryset_Head             = Head.objects.all()
    Queryset_CareerOne        = Career_One.objects.all()
    Queryset_CareerTwo        = Career_Two.objects.all()
    Queryset_CareerThree      = Career_Three.objects.all()
    Queryset_CareerFour       = Career_Four.objects.all()
    Queryset_CareerFive       = Career_Five.objects.all()
   
    
    return render(request,'careers.html',{ #common views
                                        "links"       : Queryset_Navigation_links,
                                        "footer"      : Queryset_Footer,
                                        "social"      : Queryset_Social,
                                        "others"      : Queryset_Others,
                                         #end ofcommon views
                                        "head"        : Queryset_Head,
                                        "careerone"   : Queryset_CareerOne,
                                        "careertwo"   : Queryset_CareerTwo,
                                        "careerthree" : Queryset_CareerThree,
                                        "careerone"   : Queryset_CareerFour,
                                        "careerfour"  : Queryset_CareerFive,
                                        })                                      