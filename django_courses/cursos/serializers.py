from .models import *
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = ('name', 'age', 'courses')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    lessons = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = ('name', 'lessons')