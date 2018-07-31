# Create your views here.
from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self):
        querySet = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj