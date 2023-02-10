from django.contrib import admin
from Supervision.models import *

@admin.register(TypeServer)
class TypeServerAdmin(admin.ModelAdmin):
    list_display=(
        "t_name",
        "t_version_server",
    )

    list_filter=(
        "t_name",
        "t_version_server",
    )

    search_fields=(
        "t_name",
        "t_version_server",
    )

@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    list_display=(
        "o_name",
        "o_version",
    )

    list_filter=(
        "o_name",
        "o_version",
    )

    search_fields=(
        "o_name",
        "o_version",
    )

@admin.register(HostList)
class HostListAdmin(admin.ModelAdmin):
    list_display=(
        "h_name",
        "h_ip",
        "h_os",
        "h_type_server",
        "h_status",
    )

    list_filter=(
        "h_name",
        "h_ip",
        "h_os",
        "h_type_server",
        "h_status",
    )

    search_fields=(
        "h_name",
        "h_ip"
        "h_os",
        "h_type_server",
    ),
@admin.register(JmeterJmx)
class JmeterJmxAdmin(admin.ModelAdmin):
    list_display=(
        "j_name",
        "j_scenario_path",
        )

    list_filter=(
        "j_name",
    )

    search_fields=(
        "j_name",
    )

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display=(
        "a_name",
        "a_host",
        "a_precedent_state",
        "a_actual_state",
        )

    list_filter=(
        "a_name",
        "a_host",
        "a_precedent_state",
        "a_actual_state",
    )

    search_fields=(
        "a_name",
        "a_host",
        "a_precedent_state",
        "a_actual_state",
    )

