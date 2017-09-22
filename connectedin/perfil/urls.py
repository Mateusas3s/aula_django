from django.conf.urls import url
from perfil import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^perfil/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfil/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar')

]