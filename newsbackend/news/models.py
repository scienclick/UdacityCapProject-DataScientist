# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models





class News(models.Model):
    title = models.TextField(verbose_name="title", max_length=1500)
    description = models.TextField(verbose_name="Description", max_length=10000)
    datestr = models.TextField(verbose_name="DateString", max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return self.title


class Entity(models.Model):
    releventnews = models.ForeignKey(News, related_name='entities4thisnews', on_delete=models.CASCADE, null=True, blank=True)
    entity = models.TextField(verbose_name="Entity", max_length=100)
    entity_choices = [('PERSON', 'PERSON'),
                      ('NORP', 'NORP'),
                      ('FAC', 'FAC'),
                      ('ORG', 'ORG'),
                      ('GPE', 'GPE'),
                      ('LOC', 'LOC'),
                      ('PRODUCT', 'PRODUCT'),
                      ('EVENT', 'EVENT'),
                      ('WORK_OF_ART', 'WORK_OF_ART'),
                      ('LAW', 'LAW'),
                      ('LANGUAGE', 'LANGUAGE'),
                      ('DATE', 'DATE'),
                      ('TIME', 'TIME'),
                      ('PERCENT', 'PERCENT'),
                      ('MONEY', 'MONEY'),
                      ('QUANTITY', 'QUANTITY'),
                      ('ORDINAL', 'ORDINAL'),
                      ('CARDINAL', 'CARDINAL')]
    entity_type = models.CharField(choices=entity_choices, default='PERSON', max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)
