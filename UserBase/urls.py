from django.conf.urls import url
from UserBase import views


urlpatterns = [

    url(r'^$', views.user_list),
    url(r'^(?P<no>[0-9]+)/$', views.user_id),
    # url(r'^access/(?P<token>[\w.@+-]+/$)', views.user_access),
    url(r'^access/(?P<token>[\w\.-]+)/$', views.user_access),
    # url(r'^access/?P<token>[^\s]+/$', views.user_access),
]


