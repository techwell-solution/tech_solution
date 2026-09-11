from django.db import models
from django.utils.text import slugify


class Platform(models.Model):

    name = models.CharField(
        max_length=150
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=255
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class"
    )

    image = models.ImageField(
        upload_to="platforms/",
        blank=True,
        null=True
    )

    url = models.URLField(
        blank=True,
        help_text="URL of the platform"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    featured = models.BooleanField(
        default=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)




class Service(models.Model):

    title = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    short_description = models.CharField(
        max_length=255,
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome icon class, e.g. fa-solid fa-code",
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    featured = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

class ContactMessage(models.Model):

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"