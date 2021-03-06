from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category


class CustomDraggableMPTTAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',

    )
    list_display_links = (
        'indented_title',
    )


admin.site.register(
    Category,
    CustomDraggableMPTTAdmin,

)
