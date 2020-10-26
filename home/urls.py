from django.conf.urls import url

from . import views
app_name = "home"

urlpatterns = [
    url(r'^$', views.index, name = 'homeurl'),
    url(r'^en$', views.engversion, name = 'engversion'),
]