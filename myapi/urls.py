from django.conf.urls import url
from myapi import views

urlpatterns = [
    url(r'^myapi/$', views.ConsumerList.as_view()),
    url(r'^myapi/(?P<pk>[0-9]+)/$', views.ConsumerDetail.as_view()),
    url('^myapi/(?P<country>.+)/$', views.ConsumerList.as_view()),
]
