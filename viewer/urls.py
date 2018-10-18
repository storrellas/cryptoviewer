from django.conf.urls import url

from . import views

# Set URL patterns
urlpatterns = []
urlpatterns += url('', views.IndexView.as_view()),
