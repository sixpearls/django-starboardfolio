#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings as site_settings
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.core.urlresolvers import reverse

from starboardfolio import settings
from massmedia.models import Collection
from textify.models import RenderedContentMixin, render_content
from categories.models import CategoryBase

from datetime import datetime


class ProjectCategory(CategoryBase):
    class Meta:
        verbose_name_plural = 'Project Categories'

    def get_absolute_url(self):
        slug = '/'.join(self.get_ancestors(include_self=True).values_list('slug',flat=True))
        return reverse('portfolio_category_detail', args=(), kwargs={
            'category_slug': slug,
        })

class Project(Collection):
    slug = models.SlugField(unique=False)
    content_raw = models.TextField(_('Raw input'), blank=True, default=settings.CAPTION_DEFAULT)
    category = models.ForeignKey(ProjectCategory, related_name='projects')
    date = models.DateField(default=datetime.now, blank=True, null=True)
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.caption = render_content(text=self.content_raw,self=self)
        super(Project,self).save(*args,**kwargs)

    @property
    def safe_content(self):
        return mark_safe(self.caption)

    class Meta:
        ordering = ['date', 'order', 'slug',]        
        unique_together = ("category", "slug",)

    def get_absolute_url(self):
        return reverse('portfolio_project_detail', args=(), kwargs={ # ('PortfolioProjectDetail.as_view', (), {
            'category_slug': '/'.join(self.category.get_ancestors(include_self=True).values_list('slug',flat=True)),
            'project_slug': self.slug
        })
