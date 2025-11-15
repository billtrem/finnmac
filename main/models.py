from django.db import models
from django.utils.text import slugify


# -------------------------
# Homepage Content
# -------------------------
class HomepageImage(models.Model):
    image = models.ImageField(upload_to="homepage_carousel/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or "Homepage Image"

    class Meta:
        verbose_name = "Homepage Carousel Image"
        verbose_name_plural = "Homepage Carousel Images"


# -------------------------
# Info Page
# -------------------------
class InfoPageContent(models.Model):
    portrait = models.ImageField(upload_to="info/", null=True, blank=True)
    bio = models.TextField(help_text="Finn-Mac’s bio or artist statement")
    contact_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "Info Page Content"

    class Meta:
        verbose_name = "Info Page Content"
        verbose_name_plural = "Info Page Content"


# -------------------------
# Blog
# -------------------------
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    body = models.TextField()
    preview_image = models.ImageField(upload_to="blog/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# -------------------------
# Exhibitions
# -------------------------
class Exhibition(models.Model):
    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("current", "Current"),
        ("past", "Past"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to="exhibitions/", null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.status})"


# -------------------------
# Projects
# -------------------------
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    link = models.URLField(
        null=True, blank=True, help_text="Optional external link (e.g. Bandcamp, Vimeo)"
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# -------------------------
# Services (UPDATED + EXPANDED)
# -------------------------
class Service(models.Model):
    SERVICE_CHOICES = [
        ("composer", "Composer"),
        ("post_production_audio", "Post-Production Audio"),
        ("sound_design", "Sound Design"),
        ("sound_recordist", "Sound Recordist"),
    ]

    # identity
    name = models.CharField(max_length=100, choices=SERVICE_CHOICES, unique=True)
    title = models.CharField(max_length=200, help_text="Display title for the service")
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    # content
    tagline = models.CharField(
        max_length=255,
        blank=True,
        help_text="Short one-line summary displayed under the title",
    )
    description = models.TextField(
        help_text="Main description for the top section of the service page"
    )
    image = models.ImageField(upload_to="services/", null=True, blank=True)

    # structured content (bullet lists + sections)
    areas_of_work = models.TextField(
        blank=True,
        help_text="One bullet point per line for the list of areas/services",
    )
    process = models.TextField(
        blank=True,
        help_text="Optional section describing methods, workflow, or approach",
    )

    # admin
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title or self.get_name_display())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_name_display()
