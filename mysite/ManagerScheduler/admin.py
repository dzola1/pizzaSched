from django.contrib import admin
from __future__ import unicode_literals
 
from django.contrib import admin
from models import Schedule
 
class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']