from django.contrib import admin
from django.utils.html import format_html
from .models import PageImage

@admin.register(PageImage)
class PageImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"
