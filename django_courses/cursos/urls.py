from django.conf.urls import url
from cursos.views import *

urlpatterns = [
	url(r'^cursos/$', StudentList.as_view(), name='cursos')
]