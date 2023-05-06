# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MemoryUse, SwapUse


@admin.register(MemoryUse)
class MemoryUseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'm_host',
        'm_datetime',
        'm_free_memory',
        'm_used_memory',
    )
    list_filter = ('m_host',)


@admin.register(SwapUse)
class SwapUseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        's_host',
        's_datetime',
        's_free_memory',
        's_used_memory',
    )
    list_filter = ('s_host',)
