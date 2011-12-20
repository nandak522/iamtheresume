from django.conf.urls.defaults import patterns, include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iamtheresume.views.home', name='home'),
    # url(r'^iamtheresume/', include('iamtheresume.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('users.views',
    (r'^$', 'view_homepage', {'homepage_template':'homepage.html'}, 'homepage'),
    (r'^signup/$', 'view_signup', {'signup_template':'signup.html'}, 'signup'),
    #(r'^login/$', 'view_login', {'login_template':'login.html'}, 'login'),
)
