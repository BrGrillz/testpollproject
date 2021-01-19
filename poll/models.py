from django.db import models
from django.utils.translation import ugettext_lazy as _


QUESTION_TYPES = (
    (1, 'ответ текстом'),
    (2, 'ответ с выбором одного варианта'),
    (3, 'ответ с выбором нескольких вариантов')
)


class Polls(models.Model):
    name = models.CharField(_('Название опроса'), max_length=50)
    start_date = models.DateField(_('Дата начала опроса'), )
    end_date = models.DateField(_('Дата окончания опроса'), )
    description = models.TextField(_('Описание опроса'), max_length=500)


class Questions(models.Model):
    text = models.TextField(_('Текст вопроса'), max_length=500)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name="questions")
    question_type = models.CharField(_('Тип вопроса'), max_length=50, choices=QUESTION_TYPES, default='ответ с выбором одного варианта')


class Answers(models.Model):
    text = models.TextField(_('Ответ'), max_length=500)
    is_choice = models.BooleanField(_('Выбран ли ответ пользоателем'), default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')


class Users(models.Model):
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='users')
