from utils import response
from utils import post_data
from users.forms import SignUpForm, LoginForm
from users.models import UserProfile
from django.contrib.auth import authenticate as django_authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse as url_reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from users.decorators import anonymoususer, is_admin

def view_homepage(request, homepage_template):
    user = request.user
    if user.is_authenticated():
        return response(request, homepage_template, {'message':'Welcome %s' % user.email})
    return response(request, homepage_template, {'message':'You are Anonymous'})

#TODO:@anonymous_user
def view_signup(request, signup_template):
    if request.method == 'POST':
        form = SignUpForm(post_data(request))
        if form.is_valid():
            signup_data = form.cleaned_data
            userprofile = UserProfile.objects.create_profile(email=signup_data.get('email'),
                                                             password=signup_data.get('password'),
                                                             name=signup_data.get('name'))
            return _let_user_login(request,
                                   userprofile.user,
                                   email=signup_data.get('email'),
                                   password=signup_data.get('password'))
    else:
        form = SignUpForm()
    return response(request, signup_template, {'form':form})

def _let_user_login(request, user, email, password, next=''):
    user = django_authenticate(email=email, password=password)
    django_login(request, user)
    if next:
        return HttpResponseRedirect(redirect_to=next)
    return HttpResponseRedirect(redirect_to='/')

def view_logout(request, logout_template):
    django_logout(request)
    #from users.messages import USER_LOGOUT_SUCCESSFUL
    #messages.info(request, USER_LOGOUT_SUCCESSFUL)
    return HttpResponseRedirect(redirect_to='/')
