from django.contrib import admin

from notes.models import Note


# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author",)
    fields = ("title", "text", "author", "created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("title", "author",)
