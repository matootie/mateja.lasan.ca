from django.contrib import admin

from guides.models import Tag
from guides.models import Guide


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = (
        'value',
        'parent_tag',
        'description', )
    list_display = (
        'value',
        'parent_tag', )


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'content_md',
        'content_html',
        'tags', )
    list_display = (
        'published',
        'title', )
