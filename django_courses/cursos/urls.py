from django.conf.urls import url
from cursos.views import *

urlpatterns = [
    url(r'^students/$', StudentList.as_view(), name='estudiantes'),
	url(r'^courses/$', CoursesList.as_view(), name='cursos'),
	url(r'^lessons/$', LessonsList.as_view(), name='lecciones'),
	url(r'^questions/$', MultipleChoiceQuestionsList.as_view(), name='preguntas'),
	url(r'^answers/$', SimpleAnswersList.as_view(), name='respuestas'),
]