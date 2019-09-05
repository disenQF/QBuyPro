#!/usr/bin/python3
# coding: utf-8
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'QBuyPro.settings')

app = Celery('QBuyPro',
             broker='redis://119.3.170.97:6378/3',
             backend='redis://119.3.170.97:6378/4',
             namespace='Celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
