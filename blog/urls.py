from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^http://kylianmanzini.pythonanywhere.com/$', views.post_list, name='post_list'),
]