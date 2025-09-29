from django.contrib import admin
from django.utils.html import format_html
from .models import HomepageImage, InfoPageContent, BlogPost, Exhibition, Project


# -------------------------
# Homepage Content
# -------------------------
@admin.register(HomepageImage)
class HomepageImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image Preview"


# -------------------------
# Info Page Content
# -------------------------
@admin.register(InfoPageContent)
class InfoPageContentAdmin(admin.ModelAdmin):
    list_display = ("bio", "contact_email")
    fields = ("portrait", "bio", "contact_email")


# -------------------------
# Blog
# -------------------------
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "preview_image_tag")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "body")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    readonly_fields = ("preview_image_tag",)
    exclude = ("created_at",)

    def preview_image_tag(self, obj):
        if obj.preview_image:
            return format_html('<img src="{}" width="150" />', obj.preview_image.url)
        return "-"
    preview_image_tag.short_description = "Preview Image"


# -------------------------
# Exhibitions
# -------------------------
@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "date", "location", "image_preview")
    list_filter = ("status", "date")
    search_fields = ("title", "description", "location")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "-"
    image_preview.short_description = "Exhibition Image"


# -------------------------
# Projects
# -------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "project_image_preview")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("project_image_preview",)

    def project_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "-"
    project_image_preview.short_description = "Project Image"
