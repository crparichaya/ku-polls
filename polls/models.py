import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date ended', default=None, null=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        now = timezone.localtime()
        return self.pub_date <= now

    def can_vote(self):
        now = timezone.localtime()
        if self.end_date is None:
            return self.pub_date <= now
        return self.pub_date <= now <= self.end_date


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     # votes = models.IntegerField(default=0)
#
#     @property
#     def votes(self):
#         return OneChoice.objects.filter(choice=self).count()
#
#     def __str__(self):
#         return self.choice_text
#
#
# class OneChoice(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     choice_text = models.ForeignKey(Choice, on_delete=models.CASCADE)
#     # votes = models.IntegerField(default=0)
#
#     @property
#     def question(self):
#         return self.choice_text.question
#
#     def __str__(self):
#         return self.choice_text
class Choice(models.Model):
    """Choice models for polls.
    Returns:
        models: Choice models(question, choice text, votes)
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return choice text."""
        return self.choice_text

    @property
    def votes(self):
        return Vote.objects.filter(choice=self).count()


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=0)

