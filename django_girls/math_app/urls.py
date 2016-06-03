from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sin/$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^ajax$', views.main, name='main'),
    url(r'^api/ajax_json$', views.ajaxexample),
]
