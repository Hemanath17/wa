from django.contrib import admin
from django.urls import path

from .views import home, API_used, contact
from django.views.static import serve
from django.conf.urls.satic import static
from django.conf.urls.satic import url


urlpatterns = [
    path('', home, name="home"),
    path('api/', API_used, name="api"),

    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
