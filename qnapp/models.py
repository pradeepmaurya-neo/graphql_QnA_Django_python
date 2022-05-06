from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    title = models.CharField(max_length=255, default=_('New Quizz'))

    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title


class Question(models.Model):

    SCALE = (
        (0, _('fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choices Type')),

    )

    quiz = models.ForeignKey(Quizzes, related_name='questions', on_delete=models.DO_NOTHING)

    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_('Type of Questions'))

    title = models.CharField(max_length=255, verbose_name=_('Title'))

    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))

    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))

    is_active = models.BooleanField(default=False, verbose_name=_('Active status'))


    def __str__(self):
        return self.title


class Answer(models.Model):
    questions = models.ForeignKey(Question, related_name="Answer", on_delete=models.DO_NOTHING)

    answer_text = models.CharField(max_length=255, verbose_name=_('Answer Text'))

    is_right = models.BooleanField(default=False)


    def __str__(self):
        return self.answer_text


