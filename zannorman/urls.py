from django.conf.urls import *

import zannorman.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'zannorman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', zannorman.views.home),
	url(r'^blog/$', zannorman.views.blog_base), # Teacher final
	url(r'^address/$', zannorman.views.simple_page('address.html')), # Teacher final
	url(r'^blog/(.*)/$', zannorman.views.blog), # Teacher final
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', zannorman.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', zannorman.views.file_b),
]
