from django.conf.urls import url
from golden_leash import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),

    ]
