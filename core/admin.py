from django.contrib import admin
from .models import Platform, Service, ContactMessage


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "featured",
        "is_active",
        "order",
    )

    list_filter = (
        "featured",
        "is_active",
    )

    search_fields = (
        "name",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    ordering = (
        "order",
        "name",
    )



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "is_active",
        "order",
        "created_at",
    )

    list_filter = (
        "featured",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    ordering = (
        "order",
        "title",
    )
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )