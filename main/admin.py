from django.contrib import admin
from django.utils.html import format_html
from .models import (
    HomepageImage,
    InfoPageContent,
    BlogPost,
    Exhibition,
    Project,
    Service,
)


# ==========================================================
# Homepage Images
# ==========================================================
@admin.register(HomepageImage)
class HomepageImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


# ==========================================================
# Info Page
# ==========================================================
@admin.register(InfoPageContent)
class InfoPageContentAdmin(admin.ModelAdmin):
    list_display = ("contact_email",)
    fields = ("portrait", "bio", "contact_email", "portrait_preview")
    readonly_fields = ("portrait_preview",)

    def portrait_preview(self, obj):
        if obj.portrait:
            return format_html('<img src="{}" width="180" />', obj.portrait.url)
        return "-"
    portrait_preview.short_description = "Portrait Preview"


# ==========================================================
# Blog
# ==========================================================
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "preview_image_tag")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "body")
    list_filter = ("created_at",)
    readonly_fields = ("preview_image_tag",)

    def preview_image_tag(self, obj):
        if obj.preview_image:
            return format_html('<img src="{}" width="180" />', obj.preview_image.url)
        return "-"
    preview_image_tag.short_description = "Preview"


# ==========================================================
# Exhibitions
# ==========================================================
@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "date", "location", "image_preview")
    list_filter = ("status", "date")
    search_fields = ("title", "location", "description")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="180" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


# ==========================================================
# Projects
# ==========================================================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "project_image_preview")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("project_image_preview",)

    def project_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        return "-"
    project_image_preview.short_description = "Preview"


# ==========================================================
# Services  (NEW + FULLY UPDATED)
# ==========================================================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "name",
        "is_published",
        "created_at",
        "service_image_preview",
    )
    list_filter = ("is_published", "name", "created_at")
    search_fields = ("title", "description", "name")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("service_image_preview",)

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "title", "slug", "is_published")
        }),
        ("Content", {
            "fields": ("tagline", "description", "areas_of_work", "process"),
        }),
        ("Media", {
            "fields": ("image", "service_image_preview"),
        }),
    )

    def service_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        return "-"
    service_image_preview.short_description = "Image Preview"
