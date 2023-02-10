from django.contrib import admin
from .models import *

@admin.register(DjangoApplication)
class DjangoApplicationAdmin(admin.ModelAdmin):
    list_display=(
        "d_name",
        "d_views",
        "d_url_home"
    )

    list_filter=(
        "d_name",
        "d_views",
        "d_url_home"
    )

    search_fields=(
        "d_name",
        "d_views",
        "d_url_home",
    )
