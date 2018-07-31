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

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Lesson
        fields = ('name', 'questions')

class MultipleChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = serializers.StringRelatedField(many=True)

    class Meta:
        model = MultipleChoiceQuestion
        fields = ('score', 'answers')

class SimpleAnswersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SimpleAnswer
        fields = ('order', 'answer')