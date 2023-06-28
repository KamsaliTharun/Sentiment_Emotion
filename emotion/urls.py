from django.urls import path
# from django.conf.urls import url
from . import views



from django.urls import re_path


app_name = 'emotion'

urlpatterns = [
    re_path(r'^$', views.emotion_analysis, name="emotion_anaylsis"),
    re_path(r'^type/$', views.emotion_analysis_type, name="emotion_analysis_type"),
    re_path(r'^import/$', views.emotion_analysis_import, name="emotion_analysis_import"),
]