from django.conf.urls import patterns, url

from nopims import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^nopims/', include('nopims.urls'))
)