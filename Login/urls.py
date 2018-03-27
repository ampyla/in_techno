from django.conf.urls import url, include
from Login.views import *



urlpatterns = [
    url(r'^index$', Main.as_view(), name='index'),
    url(r'^login$', LoginAuth.as_view(), name='login'),
    url(r'^detail/(?P<slug>[^/]+)/$', Detail.as_view(), name= 'detail'),
    url(r'^logout$', Logout.as_view(), name= 'logout'),


    #url(r'^accounts/login/$', Main.as_view(), name= 'main'),
]
