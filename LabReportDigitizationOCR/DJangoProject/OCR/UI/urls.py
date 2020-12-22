from django.templatetags.static import static
from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

"""path('img_upload', views.home, name='home'),"""
urlpatterns = [
    path('', views.home, name='home'),
    path('img_upload', views.home, name='home'),
    path('upload', views.uploadImage, name='uploadImage'),
    path('verify', views.verify, name='verify'),
    path('update', views.update, name='update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )