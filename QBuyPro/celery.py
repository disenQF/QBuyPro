#!/usr/bin/python3
# coding: utf-8
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'QBuyPro.settings')

app = Celery('QBuyPro',
             broker='redis://localhost:6379/3',
             backend='redis://localhost:6379/4',
             namespace='Celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
