from django.conf.urls import url

from . import views
app_name = "product"

urlpatterns = [
    url(r'', views.index, name = 'producturl'),
]