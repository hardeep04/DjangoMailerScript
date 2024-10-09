# from django.conf.urls import url
from django.urls import re_path  # or 'path' if not using regex

from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
]
