# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.fields import \
    GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Job(models.Model):
    '''
    Generic relation

    https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#generic-relations
    '''
    STATUS = (('RUNNING', 'RUNNING'),
        ('QUEUED', 'QUEUED'),
        ('COMPLETED', 'COMPLETED'),
        ('REMOVED', 'REMOVED'),
        ('DEFERRED', 'DEFERRED'),
        ('IDLE', 'IDLE'),
        ('UNKNOWN', 'UNKNOWN'))

    status = models.CharField(choices=STATUS, max_length=20)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Reduction(models.Model):
    name = models.CharField(max_length=50)
    # The relation on the related object back to this object doesn’t exist by
    # default. Setting related_query_name creates a relation from the related
    # object back to this one. This allows querying and filtering from the
    # related object.
    job = GenericRelation(Job, related_query_name='job')

class Scan(models.Model):
    reduction = models.ForeignKey(Reduction)
    name = models.CharField(max_length=100)
    job = GenericRelation(Job, related_query_name='job')
