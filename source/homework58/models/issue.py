from django.db import models

from homework58.models.issuetype import IssueType


class Issue(models.Model):
    summary = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Краткое описание'
    )
    description = models.TextField(
        max_length=254,
        null=True,
        verbose_name='Полное описание'
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
