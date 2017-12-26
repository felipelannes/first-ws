from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^item/list/', views.all_items, name='all_items'),
	url(r'^vessel/add/', views.vessel_add, name='vessel_add'),
    url(r'^vessel/list/', views.vessel_list, name='vessel_list'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/$', views.gs_add, name='gs_add'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/(?P<gs>\d+)', views.gs_items, name='gs_items'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/remove', views.vessel_remove, name='vessel_remove'),
    url(r'^upload/(?P<ASV_Project_Number>.+)/', views.upload, name='upload'),
]