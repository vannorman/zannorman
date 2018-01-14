from django.conf.urls import *

import charlievannorman.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'charlievannorman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', charlievannorman.views.home),
	url(r'^blog/$', charlievannorman.views.blog), # Teacher final
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', charlievannorman.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', charlievannorman.views.file_b),
]
