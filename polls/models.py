import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pubblication_date = models.DateTimeField('published date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pubblication_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question_rf = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
