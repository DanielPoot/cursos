from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Course(models.Model):
    student = models.ForeignKey(Student, related_name='courses', on_delete=models.CASCADE)
    order = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('student','order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.name)

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    order = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('course','order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.name)



class BooleanQuestion(models.Model):
    score = models.DecimalField(max_digits=4, decimal_places=2)
    answer = models.BooleanField()

class MultipleChoiceQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=4, decimal_places=2)

class SimpleAnswer(models.Model):
    multipleChoiceQuestion = models.ForeignKey(MultipleChoiceQuestion, related_name='answers', on_delete=models.CASCADE)
    order = models.IntegerField()
    answer = models.CharField(max_length=255)

    class Meta:
        unique_together = ('multipleChoiceQuestion', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.answer)


