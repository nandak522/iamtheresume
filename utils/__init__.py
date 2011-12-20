from django.conf import settings
from django.contrib.sites.models import Site 
from django.core.urlresolvers import reverse as url_reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.test import TestCase
from django.core.serializers import serialize

def response(request, template, context):
    return render_to_response(template, context, context_instance=RequestContext(request))

def print_json(queryset):
    print serialize("json", queryset, indent=4)

def post_data(request):
    return request.POST.copy()

def get_data(request):
    return request.GET.copy()

class TestCase(TestCase):
    def setUp(self):
        settings.DEBUG = True
    
    def tearDown(self):
        del self.client
        
    def login_as(self, email, password):
        return self.client.post(path=url_reverse('users.views.view_login'),
                                data={'email':email, 'password':password})
        
    def logout(self):
        return self.client.post(path=url_reverse('users.views.view_logout'))
    
def loggedin_userprofile(request):
    return request.user.get_profile()

def useful_params_in_context(request):
    params = {}
    params['site'] = Site.objects.get(id=settings.SITE_ID)
    if request.user.is_authenticated():
        params['userprofile'] = request.user.get_profile()
        params['userprofilegroup'] = request.user.get_profile().group_name
    #TODO:the entire params dict needs to be cached
    return params
