#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings

DEFAULT_CAPTION_DEFAULT = """title
:    The title

medium
:    awesomeness on creativity

location
:    NY, NY

other field
:    other value

This is a generic description which doesn't go into the meta data fieldset."""

DEFAULT_SETTINGS = {
    "CAPTION_DEFAULT": DEFAULT_CAPTION_DEFAULT
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'STARBOARDFOLIO_SETTINGS', {}))

globals().update(USER_SETTINGS)
