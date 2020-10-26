from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = "blog"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search', views.search),
    path('<topic>/<slug>/', views.post, name = 'post'),
    
    path('register/', views.register, name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/blog'),name='logout'),
    path('<topicname>/', views.topicview, name = 'topic'),
]