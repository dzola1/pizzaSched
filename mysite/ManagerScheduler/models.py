from django.db import models
from __future__ import unicode_literals
 
from django.db import models
 
class Schedule(models.Model):
    day = models.DateField(u'Day', help_text=u'Day of work')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Who is working and other notes', help_text=u'Employees working', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
