from django.conf.urls import url,include
from blog.views import *


urlpatterns = [
    url(r'^$', Main),
    url(r'^state/(?P<sid>\d+)/$', StateF),
]
