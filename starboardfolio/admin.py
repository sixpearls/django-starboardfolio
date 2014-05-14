#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from .models import Project, ProjectCategory
from massmedia.models import Image, CollectionRelation
from massmedia.admin import CollectionAdmin, CollectionInline
from textify.admin import RenderedContentAdminMixin

class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ProjectAdmin(RenderedContentAdminMixin):
    #class CollectionAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content_raw', 'zip_file', 'external_url', 'public', 'site', 'category')
    list_display = ('title', 'caption', 'public', 'creation_date')
    list_filter = ('site', 'creation_date', 'public')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'creation_date'
    search_fields = ('caption',)
    inlines = (CollectionInline,)

    class Media:
        js = (
            'http://code.jquery.com/jquery-1.4.2.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            'js/genericcollections.js',
        )

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)