from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.galeria, name='galeria'),
    url(r'^(?P<imagen_id>[0-9]+)/$', views.d_imagen, name='imagen'),
]