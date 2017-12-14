from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^homepage/', views.homepage, name='homepage'),
	url(r'^gs_item/', views.gs_item, name='gs_item'),
	url(r'^vessel/add/', views.vessel_add, name='vessel_add'),
    url(r'^vessel/list/', views.vessel_list, name='vessel_list'),
    url(r'^vessel/(?P<pk>\d+)/$', views.gs_infos, name='gs_infos'),
    url(r'^vessel/(?P<pk>\d+)/$', views.gs_add, name='gs_add'),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
]