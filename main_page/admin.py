#coding: utf-8
from django.contrib import admin
from .models import Ad

# Register your models here.

class AdAdmin(admin.ModelAdmin):
	list_display = ('ad_header', 'ad_content', 'ad_views',)

admin.site.register(Ad, AdAdmin)