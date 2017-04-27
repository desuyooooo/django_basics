from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^edit/(?P<pk>\d+)/$', views.Update.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.Delete.as_view(), name='delete'),
    ]
