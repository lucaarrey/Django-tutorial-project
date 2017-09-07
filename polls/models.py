from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pubblication_date = models.DateTimeField('published date')

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question_rf = models.ForeignKey(Question, on_delete=models.CASCADE)
