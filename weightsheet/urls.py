from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^gs_item/', views.gs_item, name='gs_item'),
	url(r'^vessel/add/', views.vessel_add, name='vessel_add'),
    url(r'^vessel/list/', views.vessel_list, name='vessel_list'),
    url(r'^vessel/(?P<ID_ASV_Vessel>.+)/$', views.gs_add, name='gs_add'),
    url(r'^vessel/(?P<ID_ASV_Vessel>.+)/(?P<gs>\d+)', views.gs, name='gs'),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
]