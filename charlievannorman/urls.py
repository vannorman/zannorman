from django.conf.urls import *

import charlievannorman.zanchat
import charlievannorman.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'charlievannorman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', charlievannorman.views.home),

]
