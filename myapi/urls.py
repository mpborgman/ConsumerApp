from django.conf.urls import url
from myapi import views

urlpatterns = [
    url(r'^myapi/$', views.consumer_list),
    url(r'^myapi/(?P<pk>[0-9]+)/$', views.consumer_detail),
]
