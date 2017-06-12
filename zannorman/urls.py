from django.conf.urls import patterns, url

import zannorman.zanchat
import zannorman.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zannorman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', zannorman.views.home),

	url(r'^myuservoice/report/$', zannorman.zanchat.report),
)
