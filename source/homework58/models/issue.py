from django.core.exceptions import ValidationError
from django.db import models

from homework58.models.issuetype import IssueType


def validate_summary_no_digits(value):
    if any(i.isdigit() for i in value):
        raise ValidationError('Summary must not contain numbers')


def validate_summary_capitalized(value):
    if not value[0].isupper():
        raise ValidationError('Summary must start with a capital letter')


def validate_description_no_bad_words(value):
    bad_words = ['плохое', 'оскорбительное', 'bad', 'unwanted', 'Cap-de-Mort']
    for word in bad_words:
        if word in value:
            raise ValidationError('Full description contains unwanted words')


class Issue(models.Model):
    summary = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Краткое описание',
        validators=[validate_summary_no_digits, validate_summary_capitalized]
    )
    description = models.TextField(
        max_length=254,
        null=True,
        verbose_name='Полное описание',
        validators=[validate_description_no_bad_words]
    )
    status = models.ForeignKey(
        to='homework58.Status',
        on_delete=models.PROTECT
    )
    type = models.ManyToManyField(
        to='homework58.Type',
        related_name='issues',
        through=IssueType,
        through_fields=('issue', 'type'),
        blank=True
    )
    created_date = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        verbose_name='Дата и время обновления',
        auto_now=True
    )

    def __str__(self):
        return f'{self.summary}, {self.status}, {self.type}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
