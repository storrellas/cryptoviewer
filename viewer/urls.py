from django.conf.urls import url

from . import views

# Set URL patterns
urlpatterns = []
urlpatterns += url(r'^instrument', views.TableInstrumentView.as_view(), name='instrument'),
urlpatterns += url(r'^trade', views.TableTradeView.as_view(), name='trade'),
urlpatterns += url('', views.IndexView.as_view()),
