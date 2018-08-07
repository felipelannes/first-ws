from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^vessel/add/', views.vessel_add, name='vessel_add'),
    url(r'^vessel/list/', views.vessel_list, name='vessel_list'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/$', views.vessel, name='vessel'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/remove', views.vessel_remove, name='vessel_remove'),
    url(r'^upload/(?P<ASV_Project_Number>.+)/(?P<tag>.+)/', views.upload, name='upload'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/(?P<report_id>.+)/report_settings', views.report_settings, name='report_settings'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/(?P<report_id>.+)/report_cover/', views.Weightsheet_Report.report_cover, name='report_cover'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/(?P<report_id>.+)/report_first_page/', views.Weightsheet_Report.report_first_page, name='report_first_page'),  
    url(r'^vessel/(?P<ASV_Project_Number>.+)/(?P<report_id>.+)/report_summary/', views.Weightsheet_Report.report_summary, name='report_summary'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/(?P<report_id>.+)/report_content/', views.Weightsheet_Report.report_content, name='report_content'),
    url(r'^vessel/(?P<ASV_Project_Number>.+)/list_of_report', views.list_of_report, name='list_of_report'),
    
    
    
    
     
]