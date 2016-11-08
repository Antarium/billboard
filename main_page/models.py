#coding: utf-8

from django.db import models

# Create your models here.

class Ad (models.Model):
	class Meta():
		db_table = 'ad'
		verbose_name = 'Объявление'
		verbose_name_plural = 'Объявления'
	ad_header = models.CharField(default = '', max_length = 50, blank = True, null = True)
	ad_preview = models.CharField(default = '', max_length=80, blank=True, null=True)
	ad_content = models.TextField(default = '', blank=True, null=True)
	ad_views = models.SmallIntegerField(default = 0)