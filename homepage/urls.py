from django.conf.urls import patterns, include, url

import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL+'img/favicon.ico')),
    # url(r'^homepage/', include('homepage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
