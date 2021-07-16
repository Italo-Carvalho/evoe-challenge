from django.contrib import admin
from .models import NoteBlock




@admin.register(NoteBlock)
class NoteBlockAdmin(admin.ModelAdmin):
    model = NoteBlock
