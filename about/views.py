from django.shortcuts import render

# common imports
from base.models import Navigation_Bar_Links
from base.models import Footer
from base.models import Social_Media_Footer
from base.models import Others
# end of common imports

from .models import About
from .models import Shoutout_One
from .models import Shoutout_Two
from .models import Shoutout_Three
from .models import Shoutout_Four
from .models import Features_About


def about(request):
     # comon querryset
    Queryset_Navigation_links = Navigation_Bar_Links.objects.all()
    Queryset_Footer           = Footer.objects.all()
    Queryset_Social           = Social_Media_Footer.objects.all()
    Queryset_Others           = Others.objects.all()    
    Queryset_About            = About.objects.all()
    Queryset_Shoutout_one     = Shoutout_One.objects.all()
    Queryset_Shoutout_two     = Shoutout_Two.objects.all()
    Queryset_shoutout_three   = Shoutout_Three.objects.all()
    Queryset_shoutout_four    = Shoutout_Four.objects.all()
    Queryset_Features         = Features_About.objects.all()
    # end of common querryset
    
    return render(request,'about.html',{ #common views
                                        "links"         : Queryset_Navigation_links,
                                        "footer"        : Queryset_Footer,
                                        "social"        : Queryset_Social,
                                        "others"        : Queryset_Others,
                                         #end ofcommon views
                                        "about"         : Queryset_About,
                                        "shoutoutone"   : Queryset_Shoutout_one,
                                        "shoutouttwo"   : Queryset_Shoutout_two,
                                        "shoutoutthree" : Queryset_shoutout_three,
                                        "shoutoutfour"  : Queryset_shoutout_four,
                                        "features"      : Queryset_Features,
                                         } )
    
def post(request, id):
    template = 'single_post.html'
    post = Post.objects.get(pk=id)
    context = {}
    context['post'] = post
    context['meta'] = post.as_meta()
    return render(request, template, context)