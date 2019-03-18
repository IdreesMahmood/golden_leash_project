from django.conf.urls import url
from golden_leash import views


urlpatterns = [

    url(r'^$', views.index, name="index"),
    
    url(r'^register/$', views.register, name='register'),

	url(r'^walkerProfiles/$', views.walkerProfiles, name='walkerProfiles'),
	
	url(r'^viewDogs/$', views.viewDogs, name='viewDogs'),
	
	url(r'^about/$', views.about, name='about'),
	
	url(r'^login/$', views.login, name='login'),
    ]
