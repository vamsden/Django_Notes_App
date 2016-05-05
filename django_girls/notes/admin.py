from django.contrib import admin

from .models import Note
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ["__str__"]

    class Meta:
        model = Note

admin.site.register(Note, NoteAdmin)
