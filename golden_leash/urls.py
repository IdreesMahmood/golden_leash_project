from django.conf.urls import url
from golden_leash import views


urlpatterns = [

    url(r'^$', views.index, name="index"),

    url(r'^register/$', views.register, name='register'),

    url(r'^walkerProfiles/$', views.walkerProfiles, name='walkerProfiles'),

    url(r'^viewDogs/$', views.viewDogs, name='viewDogs'),

    url(r'^about/$', views.about, name='about'),

    url(r'^login/$', views.user_login, name='login'),

    url(r'^my_account/', views.my_account, name='my_account'),

    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^password/$', views.change_password, name='change_password'),

    url(r'^remove_dog/$', views.remove_dog, name='remove_dog'),

    url(r'^add_dog/$', views.add_dog, name='add_dog'),

    url(r'^edit_account/$', views.edit_account, name='edit_account'),

    url(r'^like_walker/$', views.like_walker, name='like_walker'),

    # unused dislike button
    # url(r'^dislike_walker/$', views.dislike_walker, name='dislike_walker'),

    url(r'^walker/(?P<walker_name_slug>[\w\-]+)/$', views.show_walker, name='show_walker'),


    ]
